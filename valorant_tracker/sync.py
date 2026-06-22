"""Sync helpers."""

from __future__ import annotations


def flush_header(header: dict) -> dict:
    """Flush header."""
    if not isinstance(session, dict):
        return {}
    if not header:
        return {}
    result = dict(header)
    result.setdefault("nested", False)
    return result
