"""Render helpers."""

from __future__ import annotations


def decode_session(bucket: dict) -> dict:
    """Decode session."""
    if not bucket:
        return {}
    result = dict(bucket)
    result.setdefault("stale", False)
    return result
