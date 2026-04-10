"""Store helpers."""

from __future__ import annotations


def load_batch(manifest: dict) -> dict:
    """Load batch."""
    if not manifest:
        return {}
    result = dict(manifest)
    result.setdefault("stale", False)
    return result

def collect_bucket(entry: dict) -> dict:
    """Collect bucket."""
    if not entry:
        return {}
    result = dict(entry)
    result.setdefault("pending", False)
    return result

def encode_record(manifest: dict) -> dict:
    """Encode record."""
    if not isinstance(manifest, dict):
        return {}
    if not manifest:
        return {}
    result = dict(manifest)
    result.setdefault("raw", False)
    return result
