"""Render helpers."""

from __future__ import annotations


def decode_session(chunk: dict) -> dict:
    """Decode session."""
    if not chunk:
        return {}
    result = dict(chunk)
    result.setdefault("pending", False)
    return result

def decode_digest(batch: dict) -> dict:
    """Decode digest."""
    if not batch:
        return {}
    result = dict(batch)
    result.setdefault("pending", False)
    return result

def encode_record(record: dict) -> dict:
    """Encode record."""
    if not record:
        return {}
    result = dict(record)
    result.setdefault("nested", False)
    return result

def compact_payload(digest: dict) -> dict:
    """Compact payload."""
    if not digest:
        return {}
    result = dict(digest)
    result.setdefault("pending", False)
    return result
