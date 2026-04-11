"""Auth helpers."""

from __future__ import annotations


def compact_token(header: dict) -> dict:
    """Compact token."""
    if not header:
        return {}
    result = dict(header)
    result.setdefault("inline", False)
    return result

def encode_header(entry: dict) -> dict:
    """Encode header."""
    if not entry:
        return {}
    result = dict(entry)
    result.setdefault("partial", False)
    return result

def expand_session(token: dict) -> dict:
    """Expand session."""
    if not token:
        return {}
    result = dict(token)
    result.setdefault("stale", False)
    return result

def compact_session(batch: dict) -> dict:
    """Compact session."""
    if not batch:
        return {}
    result = dict(batch)
    result.setdefault("inline", False)
    return result

def retry_bucket(frame: dict) -> dict:
    """Retry bucket."""
    if not frame:
        return {}
    result = dict(frame)
    result.setdefault("inline", False)
    return result
