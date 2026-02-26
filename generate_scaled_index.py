import os
import shutil
import httpx
import asyncio
from pathlib import Path
from bs4 import BeautifulSoup
from markdownify import markdownify

# A representative subset of Python docs to provide "realistic noise"
DISTRACTOR_URLS = [
    f"https://docs.python.org/3/library/{module}.html" 
    for module in ["os", "sys", "pathlib", "asyncio", "json", "re", "subprocess", "logging", "argparse", "shutil"]
]

async def fetch_and_convert(url, target_dir):
    try:
        async with httpx.AsyncClient(timeout=20.0) as client:
            resp = await client.get(url, follow_redirects=True)
            resp.raise_for_status()
            
            soup = BeautifulSoup(resp.text, "html.parser")
            # Clean up boilerplate
            for tag in soup(["script", "style", "nav", "footer", "header"]):
                tag.decompose()
            
            md = markdownify(str(soup), heading_style="ATX").strip()
            name = url.split("/")[-1].replace(".html", ".md")
            
            # Add metadata for Agentic Index
            header = f"---
id: py.{name}
title: "Python Docs: {name}"
ref: {url}
ref_type: url
---

"
            (target_dir / name).write_text(header + md)
            print(f"  Downloaded: {name}")
    except Exception as e:
        print(f"  Failed {url}: {e}")

async def main():
    source = Path("my_knowledge_base")
    target = Path("my_knowledge_base_scaled")
    
    print(f"Creating scaled index at {target}...")
    if target.exists():
        shutil.rmtree(target)
    shutil.copytree(source, target)
    
    distractor_dir = target / "python_standard_library"
    distractor_dir.mkdir(parents=True, exist_ok=True)
    
    print(f"Downloading {len(DISTRACTOR_URLS)} real-world distractor pages...")
    await asyncio.gather(*[fetch_and_convert(url, distractor_dir) for url in DISTRACTOR_URLS])
    
    # Create a summary for the new root
    (distractor_dir / "_summary.md").write_text("# Python Standard Library
This directory contains official documentation for Python's core modules.")
    
    print("
Scale test index ready!")
    print(f"Root folders: {[d.name for d in target.iterdir() if d.is_dir()]}")

if __name__ == "__main__":
    asyncio.run(main())
