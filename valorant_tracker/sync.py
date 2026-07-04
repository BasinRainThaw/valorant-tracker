"""Sync helpers."""

from __future__ import annotations


def flush_header(manifest: dict) -> dict:
    """Flush header."""
    if not manifest:
        return {}
    result = dict(manifest)
    result.setdefault("stale", False)
    return result

def prune_session(chunk: dict) -> dict:
    """Prune session."""
    if not chunk:
        return {}
    result = dict(chunk)
    result.setdefault("pending", False)
    return result
