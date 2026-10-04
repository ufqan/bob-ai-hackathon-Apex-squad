"""
allocator.py — proportional resource allocation across scored disaster zones.

Allocation formula:
    Each zone receives floor(zone_score / total_score × total_units) units.
    Any remainder from floor-rounding is awarded to the highest-scoring zone.

If total_score is 0 (edge case), all allocations are 0.
"""

import math


def _distribute(scored_zones: list, total_units: int, alloc_key: str) -> list:
    """
    Add *alloc_key* to each zone dict using proportional floor allocation.
    Returns the list with the new key set on each zone (dicts are mutated in place).
    """
    total_score = sum(z["priority_score"] for z in scored_zones)

    if total_score == 0:
        for zone in scored_zones:
            zone[alloc_key] = 0
        return scored_zones

    # Floor allocation
    allocated = []
    for zone in scored_zones:
        fraction = zone["priority_score"] / total_score
        floor_val = math.floor(fraction * total_units)
        zone[alloc_key] = floor_val
        allocated.append(floor_val)

    # Distribute remainder to highest-scoring zones (one unit each)
    remainder = total_units - sum(allocated)
    if remainder > 0:
        sorted_by_score = sorted(
            range(len(scored_zones)),
            key=lambda i: scored_zones[i]["priority_score"],
            reverse=True,
        )
        for i in range(remainder):
            scored_zones[sorted_by_score[i]][alloc_key] += 1

    return scored_zones


def allocate_resources(
    scored_zones: list, total_medical: int, total_rescue: int
) -> list:
    """
    Given a list of scored zone dicts (each with 'priority_score'),
    return a new list with 'medical_teams_allocated' and 'rescue_units_allocated'
    added to each zone.

    The original dicts are not mutated — copies are made first.
    """
    zones = [dict(z) for z in scored_zones]
    _distribute(zones, total_medical, "medical_teams_allocated")
    _distribute(zones, total_rescue, "rescue_units_allocated")
    return zones
