"""Clean cached markdown files and extract metadata."""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from pathlib import Path


@dataclass
class DocPage:
    """A preprocessed documentation page."""

    path: Path
    slug: str
    title: str
    content: str
    headings: list[str] = field(default_factory=list)
    word_count: int = 0


def _extract_title(text: str) -> str:
    """Extract the first H1 heading, or fall back to first heading of any level."""
    match = re.search(r"^#\s+(.+)$", text, re.MULTILINE)
    if match:
        return match.group(1).strip()
    match = re.search(r"^#{1,6}\s+(.+)$", text, re.MULTILINE)
    if match:
        return match.group(1).strip()
    return "Untitled"


def _extract_headings(text: str) -> list[str]:
    """Extract all markdown headings."""
    return [m.group(1).strip() for m in re.finditer(r"^#{1,6}\s+(.+)$", text, re.MULTILINE)]


def _clean_markdown(text: str) -> str:
    """Remove leftover navigation artifacts and excessive whitespace."""
    # Remove lines that are just links with no context (nav remnants)
    lines = text.split("\n")
    cleaned: list[str] = []
    for line in lines:
        stripped = line.strip()
        # Skip lines that are only a bare URL
        if re.match(r"^https?://\S+$", stripped):
            continue
        # Skip lines like "[Skip to content](#...)"
        if re.match(r"^\[Skip to .+\]\(#", stripped):
            continue
        cleaned.append(line)

    text = "\n".join(cleaned)
    # Collapse 3+ consecutive blank lines to 2
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def preprocess_page(path: Path, root_dir: Path | None = None) -> DocPage:
    """Read a markdown file and return a cleaned ``DocPage``."""
    raw = path.read_text(encoding="utf-8")
    content = _clean_markdown(raw)
    title = _extract_title(content)
    headings = _extract_headings(content)
    word_count = len(content.split())
    
    if root_dir:
        # Create a path-based slug: "dir-subdir-file"
        rel_path = path.relative_to(root_dir)
        slug = str(rel_path.with_suffix("")).replace("/", "-").replace("_", "-")
    else:
        slug = path.stem

    return DocPage(
        path=path,
        slug=slug,
        title=title,
        content=content,
        headings=headings,
        word_count=word_count,
    )


def preprocess_corpus(paths: list[Path], root_dir: Path | None = None) -> list[DocPage]:
    """Preprocess a list of markdown files."""
    return [preprocess_page(p, root_dir) for p in paths]
