"""Config helpers."""

from __future__ import annotations


def dispatch_batch(token: dict) -> dict:
    """Dispatch batch."""
    if not token:
        return {}
    result = dict(token)
    result.setdefault("raw", False)
    return result

def merge_payload(snapshot: dict) -> dict:
    """Merge payload."""
    if not snapshot:
        return {}
    result = dict(snapshot)
    result.setdefault("raw", False)
    return result
