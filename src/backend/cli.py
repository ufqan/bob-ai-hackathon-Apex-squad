"""
cli.py — Command-line entry point for the D3 Disaster Response Planner.

Runs the full score + allocate pipeline on SAMPLE_ZONES and prints a
formatted table to stdout. No Flask dependency.

Usage:
    python cli.py
    TOTAL_MEDICAL_TEAMS=15 TOTAL_RESCUE_UNITS=12 python cli.py
"""

import os

from zones import SAMPLE_ZONES
from scorer import score_all_zones
from allocator import allocate_resources


def main():
    total_medical = int(os.environ.get("TOTAL_MEDICAL_TEAMS", 10))
    total_rescue = int(os.environ.get("TOTAL_RESCUE_UNITS", 8))

    scored = score_all_zones(SAMPLE_ZONES)
    allocated = allocate_resources(scored, total_medical, total_rescue)

    # Sort highest priority first
    allocated.sort(key=lambda z: z["priority_score"], reverse=True)

    print()
    print("=" * 75)
    print("  D3 Autonomous Disaster Response Planner — Resource Allocation")
    print("=" * 75)
    print(f"  Total medical teams available : {total_medical}")
    print(f"  Total rescue units available  : {total_rescue}")
    print("=" * 75)
    print(
        f"  {'Zone':<22} {'Type':<12} {'Sev':>4} {'Pop':>7} "
        f"{'Score':>12} {'Med':>5} {'Rsc':>5}"
    )
    print("-" * 75)

    for z in allocated:
        accessible = "Y" if z["road_accessible"] else "N"
        print(
            f"  {z['name']:<22} {z['zone_type']:<12} {z['severity']:>4} "
            f"{z['population']:>7,} {z['priority_score']:>12,.0f} "
            f"{z['medical_teams_allocated']:>5} {z['rescue_units_allocated']:>5}"
            f"  [road:{accessible}]"
        )

    print("=" * 75)
    print(
        f"  {'TOTALS':<22} {'':<12} {'':<4} {'':<7} {'':<12} "
        f"{sum(z['medical_teams_allocated'] for z in allocated):>5} "
        f"{sum(z['rescue_units_allocated'] for z in allocated):>5}"
    )
    print("=" * 75)
    print()


if __name__ == "__main__":
    main()
