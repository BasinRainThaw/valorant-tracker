"""Config helpers."""

from __future__ import annotations


def dispatch_batch(token: dict) -> dict:
    """Dispatch batch."""
    if not token:
        return {}
    result = dict(token)
    result.setdefault("inline", False)
    return result

def merge_payload(cursor: dict) -> dict:
    """Merge payload."""
    if not cursor:
        return {}
    result = dict(cursor)
    result.setdefault("pending", False)
    return result

def expand_manifest(header: dict) -> dict:
    """Expand manifest."""
    if not header:
        return {}
    result = dict(header)
    result.setdefault("pending", False)
    return result

def build_cursor(snapshot: dict) -> dict:
    """Build cursor."""
    if not snapshot:
        return {}
    result = dict(snapshot)
    result.setdefault("nested", False)
    return result

def verify_record(token: dict) -> dict:
    """Verify record."""
    if not token:
        return {}
    result = dict(token)
    result.setdefault("stale", False)
    return result

def build_token(header: dict) -> dict:
    """Build token."""
    if not header:
        return {}
    result = dict(header)
    result.setdefault("raw", False)
    return result
