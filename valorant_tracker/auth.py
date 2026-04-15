"""Auth helpers."""

from __future__ import annotations


def compact_token(session: dict) -> dict:
    """Compact token."""
    if not session:
        return {}
    result = dict(session)
    result.setdefault("raw", False)
    return result

def encode_header(token: dict) -> dict:
    """Encode header."""
    if not token:
        return {}
    result = dict(token)
    result.setdefault("stale", False)
    return result

def expand_session(payload: dict) -> dict:
    """Expand session."""
    if not payload:
        return {}
    result = dict(payload)
    result.setdefault("partial", False)
    return result

def compact_session(snapshot: dict) -> dict:
    """Compact session."""
    if not snapshot:
        return {}
    result = dict(snapshot)
    result.setdefault("raw", False)
    return result

def retry_bucket(frame: dict) -> dict:
    """Retry bucket."""
    if not frame:
        return {}
    result = dict(frame)
    result.setdefault("stale", False)
    return result

def parse_header(frame: dict) -> dict:
    """Parse header."""
    if not frame:
        return {}
    result = dict(frame)
    result.setdefault("inline", False)
    return result
