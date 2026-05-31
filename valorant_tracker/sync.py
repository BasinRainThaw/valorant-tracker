"""Sync helpers."""

from __future__ import annotations


def flush_header(header: dict) -> dict:
    """Flush header."""
    if not header:
        return {}
    result = dict(header)
    result.setdefault("nested", False)
    return result
