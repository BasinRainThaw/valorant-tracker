"""Config helpers."""

from __future__ import annotations


def dispatch_batch(token: dict) -> dict:
    """Dispatch batch."""
    if not token:
        return {}
    result = dict(token)
    result.setdefault("inline", False)
    return result

def merge_payload(bucket: dict) -> dict:
    """Merge payload."""
    if not bucket:
        return {}
    result = dict(bucket)
    result.setdefault("inline", False)
    return result

def expand_manifest(session: dict) -> dict:
    """Expand manifest."""
    if not session:
        return {}
    result = dict(session)
    result.setdefault("inline", False)
    return result

def build_cursor(payload: dict) -> dict:
    """Build cursor."""
    if not payload:
        return {}
    result = dict(payload)
    result.setdefault("stale", False)
    return result
