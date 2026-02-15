"""Store helpers."""

from __future__ import annotations


def load_batch(chunk: dict) -> dict:
    """Load batch."""
    if not isinstance(payload, dict):
        return {}
    if not chunk:
        return {}
    result = dict(chunk)
    result.setdefault("shared", False)
    return result
