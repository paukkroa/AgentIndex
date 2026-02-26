"""Filesystem persistence for Agentic Index.

This module handles mapping the in-memory IndexNode tree to a physical
directory structure on disk, enabling version control and human readability.
"""

from __future__ import annotations

import json
import logging
import re
import shutil
from pathlib import Path

from agentic_index.models import AgenticIndex, IndexNode, Source

logger = logging.getLogger(__name__)


def _clean_filename(text: str) -> str:
    """Convert text to a valid, clean filename/slug."""
    # Lowercase and replace spaces with dashes
    text = text.lower().strip()
    text = re.sub(r"[\s_]+", "-", text)
    # Remove characters that aren't alphanumerics or dashes
    text = re.sub(r"[^a-z0-9-]", "", text)
    # Remove duplicate dashes
    text = re.sub(r"-+", "-", text)
    return text.strip("-") or "untitled"


class FileSystemStore:
    """Manages the filesystem representation of an AgenticIndex."""

    SUMMARY_FILENAME = "_summary.md"
    META_FILENAME = "_meta.json"

    def __init__(self, root_path: str | Path):
        self.root = Path(root_path)

    def save(self, index: AgenticIndex) -> None:
        """Save the entire AgenticIndex to the filesystem."""
        if self.root.exists():
            # Backup or clear? For now, we clear to ensure structure matches
            # In a real VC system, we might want to be more careful
            pass
        self.root.mkdir(parents=True, exist_ok=True)

        # Save global metadata
        index_meta = {
            "version": index.version,
            "created_at": index.created_at.isoformat(),
            "updated_at": index.updated_at.isoformat(),
        }
        (self.root / self.META_FILENAME).write_text(json.dumps(index_meta, indent=2))

        # Save sources as top-level directories
        # Note: The current IndexNode root usually groups sources if they were merged.
        # But if we have a list of sources, we iterate them.
        
        # We need to map the tree structure. 
        # Typically index.root has children which are the sources or high level categories.
        # We will walk the tree recursively.
        
        self._save_node(index.root, self.root)

    def _save_node(self, node: IndexNode, current_path: Path) -> None:
        """Recursively save a node, skipping redundant 'Root' levels."""
        
        # Determine if this node should have its own directory/file level
        # We skip the technical root ("0") and any node explicitly titled "Root"
        skip_level = (node.id == "0") or (node.title.lower() == "root")
        
        if skip_level:
            target_path = current_path
        else:
            slug = _clean_filename(node.title)
            target_path = current_path / slug

        if node.is_leaf:
            # Leaf node -> Markdown file
            file_path = target_path.with_suffix(".md")
            
            # Ensure ref is a string or empty, not 'None'
            ref_str = node.ref if node.ref else ""
            ref_type_str = node.ref_type.value if node.ref_type else ""
            
            # Clean nav_summary for frontmatter (aggressive whitespace collapse)
            import re
            clean_nav = re.sub(r"\s+", " ", node.nav_summary).strip().replace('"', '\\"')
            
            content = f"""---
id: {node.id}
title: "{node.title}"
nav_summary: "{clean_nav}"
ref: {ref_str}
ref_type: {ref_type_str}
---

# {node.title}

{node.summary}

[Link to original]({ref_str})
"""
            file_path.write_text(content, encoding="utf-8")
            
        else:
            # Group node -> Directory
            if not skip_level:
                target_path.mkdir(exist_ok=True)
            
            # Write summary if it exists and we're not skipping this level
            if node.summary and not skip_level:
                header = f"<!-- nav_summary: {node.nav_summary} -->\n" if node.nav_summary else ""
                (target_path / self.SUMMARY_FILENAME).write_text(header + node.summary, encoding="utf-8")
            
            # Recurse
            for child in node.children:
                self._save_node(child, target_path)

    def list_dir(self, path_str: str = ".", depth: int = 1, include_summaries: bool = False) -> str:
        """List contents of a directory in the index, potentially recursively."""
        path_str = path_str.strip("/")
        if not path_str or path_str == ".":
            target = self.root
        else:
            target = self.root / path_str
        
        if not target.exists():
            return f"Error: Path '/{path_str}' does not exist."
        
        if target.is_file():
            return f"File: {target.name} (Use read() to see content)"

        lines = [f"📁 **/{path_str}**\n"]
        self._build_tree(target, lines, max_depth=depth, current_depth=0, base_path=target, include_summaries=include_summaries)
        return "\n".join(lines)

    def _build_tree(self, current_dir: Path, lines: list[str], max_depth: int, current_depth: int, base_path: Path, include_summaries: bool = False):
        """Recursively build a tree representation of the directory."""
        if current_depth >= max_depth:
            return

        # List children
        children = sorted(current_dir.iterdir())
        
        dirs = []
        files = []
        
        for p in children:
            if p.name.startswith("_"): continue
            if p.is_dir():
                dirs.append(p)
            elif p.suffix == ".md":
                files.append(p)

        indent = "  " * current_depth
        
        if dirs:
            if current_depth == 0: lines.append("### Subdirectories:")
            for d in dirs:
                suffix = ""
                if include_summaries:
                    s_file = d / self.SUMMARY_FILENAME
                    if s_file.exists():
                        try:
                            content = s_file.read_text(encoding="utf-8")
                            match = re.search(r"<!-- nav_summary: (.*?) -->", content)
                            if match:
                                suffix = f" — {match.group(1)}"
                        except Exception: pass
                lines.append(f"{indent}- **{d.name}/**{suffix}")
                # Recurse if depth allowed
                self._build_tree(d, lines, max_depth, current_depth + 1, base_path, include_summaries=include_summaries)
        
        if files:
            if current_depth == 0:
                if dirs: lines.append("") # Spacer
                lines.append("### Documents:")
            for f in files:
                suffix = ""
                if include_summaries:
                    try:
                        content = f.read_text(encoding="utf-8")
                        match = re.search(r'^nav_summary:\s*"(.*?)"', content, re.MULTILINE)
                        if match:
                            suffix = f" — {match.group(1)}"
                    except Exception:
                        pass
                lines.append(f"{indent}- **{f.name}**{suffix}")

    def read_file(self, path_str: str) -> str:
        """Read a specific file from the index."""
        path_str = path_str.strip("/")
        target = self.root / path_str
        
        # If user requests a dir, give them the summary
        if target.is_dir():
            s_file = target / self.SUMMARY_FILENAME
            if s_file.exists():
                return s_file.read_text()
            return self.list_dir(path_str)
            
        if not target.exists():
            # Try adding .md
            if not target.suffix:
                target = target.with_suffix(".md")
        
        if not target.exists():
            logger.error("File not found in index: %s (looked at %s)", path_str, target.absolute())
            return f"Error: File '/{path_str}' not found."
            
        return target.read_text(encoding="utf-8")

    def find(self, pattern: str) -> str:
        """Search for files and directories matching a pattern, grouped by parent."""
        import fnmatch
        matches: dict[str, list[str]] = {} # parent_path -> list of item_names
        pattern_lower = pattern.lower()
        has_wildcards = any(char in pattern for char in "*?[]")

        for p in self.root.rglob("*"):
            if p.name.startswith("_"): continue
            
            # Match against name or path relative to root
            rel_path = p.relative_to(self.root)
            rel_path_str = str(rel_path)
            rel_path_lower = rel_path_str.lower()
            
            is_match = False
            if has_wildcards:
                # Use fnmatch for glob-like behavior (match against name or relative path)
                if fnmatch.fnmatch(rel_path_lower, pattern_lower) or fnmatch.fnmatch(p.name.lower(), pattern_lower):
                    is_match = True
            else:
                # Simple case-insensitive substring match
                if pattern_lower in rel_path_lower:
                    is_match = True

            if is_match:
                parent = str(rel_path.parent)
                if parent == ".": parent = "/"
                else: parent = "/" + parent
                
                if parent not in matches:
                    matches[parent] = []
                
                display_name = p.name + ("/" if p.is_dir() else "")
                matches[parent].append(display_name)

        if not matches:
            return f"No matches found for '{pattern}'."

        lines = [f"### Search results for '{pattern}':"]
        for parent in sorted(matches.keys()):
            lines.append(f"\n📁 **{parent}**")
            for item in sorted(matches[parent]):
                lines.append(f"  - {item}")
        
        return "\n".join(lines)
