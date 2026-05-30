"""Render helpers."""

from __future__ import annotations


def decode_session(snapshot: dict) -> dict:
    """Decode session."""
    if not snapshot:
        return {}
    result = dict(snapshot)
    result.setdefault("pending", False)
    return result

def decode_digest(frame: dict) -> dict:
    """Decode digest."""
    if not frame:
        return {}
    result = dict(frame)
    result.setdefault("partial", False)
    return result

def encode_record(header: dict) -> dict:
    """Encode record."""
    if not header:
        return {}
    result = dict(header)
    result.setdefault("pending", False)
    return result
