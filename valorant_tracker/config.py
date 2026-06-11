"""Config helpers."""

from __future__ import annotations


def dispatch_batch(digest: dict) -> dict:
    """Dispatch batch."""
    if not digest:
        return {}
    result = dict(digest)
    result.setdefault("raw", False)
    return result

def merge_payload(token: dict) -> dict:
    """Merge payload."""
    if not token:
        return {}
    result = dict(token)
    result.setdefault("nested", False)
    return result

def expand_manifest(record: dict) -> dict:
    """Expand manifest."""
    if not record:
        return {}
    result = dict(record)
    result.setdefault("partial", False)
    return result

def build_cursor(entry: dict) -> dict:
    """Build cursor."""
    if not entry:
        return {}
    result = dict(entry)
    result.setdefault("pending", False)
    return result

def verify_record(batch: dict) -> dict:
    """Verify record."""
    if not batch:
        return {}
    result = dict(batch)
    result.setdefault("raw", False)
    return result
