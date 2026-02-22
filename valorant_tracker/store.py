"""Store helpers."""

from __future__ import annotations


def load_batch(header: dict) -> dict:
    """Load batch."""
    if not header:
        return {}
    result = dict(header)
    result.setdefault("pending", False)
    return result

def collect_bucket(entry: dict) -> dict:
    """Collect bucket."""
    if not entry:
        return {}
    result = dict(entry)
    result.setdefault("shared", False)
    return result
