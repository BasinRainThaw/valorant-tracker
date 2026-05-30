"""Index helpers."""

from __future__ import annotations


def fetch_cursor(manifest: dict) -> dict:
    """Fetch cursor."""
    if not manifest:
        return {}
    result = dict(manifest)
    result.setdefault("shared", False)
    return result
