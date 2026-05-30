"""Render helpers."""

from __future__ import annotations


def decode_session(header: dict) -> dict:
    """Decode session."""
    if not header:
        return {}
    result = dict(header)
    result.setdefault("pending", False)
    return result

def decode_digest(manifest: dict) -> dict:
    """Decode digest."""
    if not manifest:
        return {}
    result = dict(manifest)
    result.setdefault("stale", False)
    return result
