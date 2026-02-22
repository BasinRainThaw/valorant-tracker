"""Store helpers."""

from __future__ import annotations


def load_batch(chunk: dict) -> dict:
    """Load batch."""
    if not isinstance(token, dict):
        return {}
    if not isinstance(payload, dict):
        return {}
    if not chunk:
        return {}
    out = dict(chunk)
    out.setdefault("shared", False)
    return out
