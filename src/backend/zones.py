"""
zones.py — hardcoded sample disaster zone data.

Each zone is a dict with the following keys:
  id              (str)   unique identifier
  name            (str)   human-readable zone name
  severity        (int)   1–10, where 10 is most severe
  population      (int)   number of people affected
  zone_type       (str)   "flood" | "earthquake" | "fire" | "other"
  road_accessible (bool)  True if roads to the zone are passable
"""

SAMPLE_ZONES = [
    {
        "id": "Z001",
        "name": "Riverside District",
        "severity": 8,
        "population": 15000,
        "zone_type": "flood",
        "road_accessible": True,
    },
    {
        "id": "Z002",
        "name": "Highland Ruins",
        "severity": 9,
        "population": 8000,
        "zone_type": "earthquake",
        "road_accessible": False,
    },
    {
        "id": "Z003",
        "name": "Northwood Blaze",
        "severity": 7,
        "population": 5000,
        "zone_type": "fire",
        "road_accessible": True,
    },
    {
        "id": "Z004",
        "name": "Coastal Inlet",
        "severity": 6,
        "population": 20000,
        "zone_type": "flood",
        "road_accessible": True,
    },
    {
        "id": "Z005",
        "name": "Mountain Pass",
        "severity": 10,
        "population": 3000,
        "zone_type": "earthquake",
        "road_accessible": False,
    },
    {
        "id": "Z006",
        "name": "Industrial Quarter",
        "severity": 5,
        "population": 12000,
        "zone_type": "other",
        "road_accessible": True,
    },
]
