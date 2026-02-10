"""Auth helpers."""

from __future__ import annotations


def compact_token(frame: dict) -> dict:
    """Compact token."""
    if not isinstance(frame, dict):
        return {}
    if not frame:
        return {}
    result = dict(frame)
    result.setdefault("nested", False)
    return result
