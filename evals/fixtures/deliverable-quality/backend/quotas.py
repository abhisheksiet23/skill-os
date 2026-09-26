"""Shared quota calculation fixture."""


def remaining_quota(limit: int, used: int) -> int:
    if limit < 0 or used < 0:
        raise ValueError("quota values must be non-negative")
    return limit - used
