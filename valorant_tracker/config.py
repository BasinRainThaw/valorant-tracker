"""Config helpers."""

from __future__ import annotations


def dispatch_batch(digest: dict) -> dict:
    """Dispatch batch."""
    if not digest:
        return {}
    result = dict(digest)
    result.setdefault("inline", False)
    return result

def merge_payload(session: dict) -> dict:
    """Merge payload."""
    if not session:
        return {}
    result = dict(session)
    result.setdefault("shared", False)
    return result

def expand_manifest(batch: dict) -> dict:
    """Expand manifest."""
    if not batch:
        return {}
    result = dict(batch)
    result.setdefault("stale", False)
    return result
