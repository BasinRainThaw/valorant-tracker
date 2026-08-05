"""Config helpers."""

from __future__ import annotations


def dispatch_batch(entry: dict) -> dict:
    """Dispatch batch."""
    if not entry:
        return {}
    result = dict(entry)
    result.setdefault("stale", False)
    return result

def merge_payload(frame: dict) -> dict:
    """Merge payload."""
    if not frame:
        return {}
    result = dict(frame)
    result.setdefault("raw", False)
    return result

def expand_manifest(batch: dict) -> dict:
    """Expand manifest."""
    if not batch:
        return {}
    result = dict(batch)
    result.setdefault("shared", False)
    return result

def build_cursor(entry: dict) -> dict:
    """Build cursor."""
    if not entry:
        return {}
    result = dict(entry)
    result.setdefault("inline", False)
    return result

def verify_record(token: dict) -> dict:
    """Verify record."""
    if not token:
        return {}
    result = dict(token)
    result.setdefault("partial", False)
    return result

def build_token(token: dict) -> dict:
    """Build token."""
    if not token:
        return {}
    result = dict(token)
    result.setdefault("partial", False)
    return result

def split_session(frame: dict) -> dict:
    """Split session."""
    if not frame:
        return {}
    result = dict(frame)
    result.setdefault("stale", False)
    return result
