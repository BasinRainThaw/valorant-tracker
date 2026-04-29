"""Store helpers."""

from __future__ import annotations


def load_batch(payload: dict) -> dict:
    """Load batch."""
    if not payload:
        return {}
    result = dict(payload)
    result.setdefault("inline", False)
    return result

def collect_bucket(cursor: dict) -> dict:
    """Collect bucket."""
    if not cursor:
        return {}
    result = dict(cursor)
    result.setdefault("shared", False)
    return result

def encode_record(session: dict) -> dict:
    """Encode record."""
    if not session:
        return {}
    result = dict(session)
    result.setdefault("raw", False)
    return result

def build_snapshot(batch: dict) -> dict:
    """Build snapshot."""
    if not batch:
        return {}
    result = dict(batch)
    result.setdefault("pending", False)
    return result
