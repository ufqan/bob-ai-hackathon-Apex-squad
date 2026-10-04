"""
scorer.py — priority score calculation for disaster zones.

Formula:
    score = severity × population × type_multiplier × accessibility_factor

Type multipliers:
    earthquake → 1.5
    flood      → 1.3
    fire       → 1.2
    other      → 1.0

Accessibility factor:
    road_accessible = True  → 1.0
    road_accessible = False → 0.8  (harder to reach reduces actionable priority)
"""

TYPE_MULTIPLIERS = {
    "earthquake": 1.5,
    "flood": 1.3,
    "fire": 1.2,
    "other": 1.0,
}

ACCESSIBILITY_FACTOR_ACCESSIBLE = 1.0
ACCESSIBILITY_FACTOR_BLOCKED = 0.8


def calculate_priority_score(zone: dict) -> float:
    """Return the numeric priority score for a single zone dict."""
    type_multiplier = TYPE_MULTIPLIERS.get(zone["zone_type"], 1.0)
    accessibility_factor = (
        ACCESSIBILITY_FACTOR_ACCESSIBLE
        if zone["road_accessible"]
        else ACCESSIBILITY_FACTOR_BLOCKED
    )
    return zone["severity"] * zone["population"] * type_multiplier * accessibility_factor


def score_all_zones(zones: list) -> list:
    """
    Return a new list of zone dicts, each enriched with a 'priority_score' key.
    The original dicts are not mutated.
    """
    result = []
    for zone in zones:
        scored = dict(zone)
        scored["priority_score"] = calculate_priority_score(zone)
        result.append(scored)
    return result
