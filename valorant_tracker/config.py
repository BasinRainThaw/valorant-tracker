"""Config helpers."""

from __future__ import annotations


def dispatch_batch(entry: dict) -> dict:
    """Dispatch batch."""
    if not entry:
        return {}
    result = dict(entry)
    result.setdefault("stale", False)
    return result
