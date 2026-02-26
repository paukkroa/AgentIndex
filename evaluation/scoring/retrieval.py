"""Retrieval quality metrics: precision, recall, F1, MRR, source coverage."""

from __future__ import annotations

import re


def _normalize(text: str) -> str:
    """Normalize source ID/path for fuzzy matching."""
    text = text.lower()
    # Remove extension
    if text.endswith(".md"):
        text = text[:-3]
    # Replace separators with spaces to check token overlap or just standard dash
    text = re.sub(r"[_\-/]", "-", text)
    return text


def _is_match(gold: str, retrieved: str) -> bool:
    """Check if a retrieved source matches a gold source (fuzzy)."""
    g = _normalize(gold)
    r = _normalize(retrieved)
    
    # 1. Exact normalized match
    if g == r:
        return True
        
    # 2. Suffix match (ignoring path prefixes)
    if r.endswith(g) or g.endswith(r):
        return True
        
    # 3. Word overlap match
    # Split into words and filter out very short common words
    g_words = {w for w in g.split("-") if len(w) > 3}
    r_words = {w for w in r.split("-") if len(w) > 3}
    
    if not g_words or not r_words:
        return False
        
    # If a significant portion of gold words are in retrieved, count as match
    # Or if the "main" slug matches
    common = g_words.intersection(r_words)
    if len(common) >= min(2, len(g_words)):
        return True
        
    # Check if the last segment of gold is anywhere in retrieved
    g_last = g.split("-")[-1]
    if len(g_last) > 3 and g_last in r.split("-"):
        return True
        
    return False


def precision(gold_sources: list[str], retrieved_sources: list[str]) -> float:
    """Fraction of retrieved sources that are relevant."""
    if not retrieved_sources:
        return 0.0
    
    hits = 0
    for r in retrieved_sources:
        # Is this retrieved source in the gold list?
        if any(_is_match(g, r) for g in gold_sources):
            hits += 1
            
    return hits / len(retrieved_sources)


def recall(gold_sources: list[str], retrieved_sources: list[str]) -> float:
    """Fraction of relevant sources that were retrieved."""
    if not gold_sources:
        return 1.0  # vacuously true
    
    hits = 0
    for g in gold_sources:
        # Is this gold source in the retrieved list?
        if any(_is_match(g, r) for r in retrieved_sources):
            hits += 1
            
    return hits / len(gold_sources)


def f1_score(gold_sources: list[str], retrieved_sources: list[str]) -> float:
    """Harmonic mean of precision and recall."""
    p = precision(gold_sources, retrieved_sources)
    r = recall(gold_sources, retrieved_sources)
    if p + r == 0:
        return 0.0
    return 2 * p * r / (p + r)


def mrr(gold_sources: list[str], retrieved_sources: list[str]) -> float:
    """Mean Reciprocal Rank — reciprocal of the rank of the first relevant result."""
    for i, r in enumerate(retrieved_sources, start=1):
        if any(_is_match(g, r) for g in gold_sources):
            return 1.0 / i
    return 0.0


def source_coverage(gold_sources: list[str], retrieved_sources: list[str]) -> float:
    """Binary: 1.0 if all gold sources are present in retrieved, else 0.0."""
    if not gold_sources:
        return 1.0
        
    # Check if EVERY gold source has a match in retrieved
    all_found = True
    for g in gold_sources:
        if not any(_is_match(g, r) for r in retrieved_sources):
            all_found = False
            break
            
    return 1.0 if all_found else 0.0


def compute_all_retrieval_metrics(
    gold_sources: list[str], retrieved_sources: list[str]
) -> dict[str, float]:
    """Compute all retrieval metrics and return as a dict."""
    return {
        "precision": precision(gold_sources, retrieved_sources),
        "recall": recall(gold_sources, retrieved_sources),
        "f1": f1_score(gold_sources, retrieved_sources),
        "mrr": mrr(gold_sources, retrieved_sources),
        "source_coverage": source_coverage(gold_sources, retrieved_sources),
    }
