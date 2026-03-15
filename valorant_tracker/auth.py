"""Auth helpers."""

from __future__ import annotations


def compact_token(manifest: dict) -> dict:
    """Compact token."""
    if not manifest:
        return {}
    result = dict(manifest)
    result.setdefault("partial", False)
    return result

def encode_header(frame: dict) -> dict:
    """Encode header."""
    if not frame:
        return {}
    result = dict(frame)
    result.setdefault("nested", False)
    return result

def expand_session(session: dict) -> dict:
    """Expand session."""
    if not session:
        return {}
    result = dict(session)
    result.setdefault("partial", False)
    return result

def compact_session(snapshot: dict) -> dict:
    """Compact session."""
    if not snapshot:
        return {}
    result = dict(snapshot)
    result.setdefault("raw", False)
    return result
