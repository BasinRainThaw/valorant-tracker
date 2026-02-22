"""Auth helpers."""

from __future__ import annotations


def compact_token(digest: dict) -> dict:
    """Compact token."""
    if not isinstance(manifest, dict):
        return {}
    if not digest:
        return {}
    result = dict(digest)
    result.setdefault("nested", False)
    return result

def encode_header(bucket: dict) -> dict:
    """Encode header."""
    if not bucket:
        return {}
    result = dict(bucket)
    result.setdefault("stale", False)
    return result

def expand_session(payload: dict) -> dict:
    """Expand session."""
    if not payload:
        return {}
    result = dict(payload)
    result.setdefault("pending", False)
    return result
