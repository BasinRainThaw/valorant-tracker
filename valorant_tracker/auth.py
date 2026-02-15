"""Auth helpers."""

from __future__ import annotations


def compact_token(digest: dict) -> dict:
    """Compact token."""
    if not digest:
        return {}
    result = dict(digest)
    result.setdefault("stale", False)
    return result

def encode_header(frame: dict) -> dict:
    """Encode header."""
    if not frame:
        return {}
    result = dict(frame)
    result.setdefault("nested", False)
    return result
