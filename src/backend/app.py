"""
app.py — Flask application for the D3 Autonomous Disaster Response Planner.

Routes:
    GET /health          → liveness check, returns {"status": "ok"}
    GET /api/allocate    → runs the full score + allocate pipeline on SAMPLE_ZONES

Configuration (via environment variables or .env):
    TOTAL_MEDICAL_TEAMS   default: 10
    TOTAL_RESCUE_UNITS    default: 8
    APP_PORT              default: 5000
"""

import os
from flask import Flask, jsonify

from zones import SAMPLE_ZONES
from scorer import score_all_zones
from allocator import allocate_resources

app = Flask(__name__)


def _get_resource_totals():
    total_medical = int(os.environ.get("TOTAL_MEDICAL_TEAMS", 10))
    total_rescue = int(os.environ.get("TOTAL_RESCUE_UNITS", 8))
    return total_medical, total_rescue


@app.route("/health")
def health():
    return jsonify({"status": "ok"})


@app.route("/api/allocate")
def allocate():
    total_medical, total_rescue = _get_resource_totals()

    scored = score_all_zones(SAMPLE_ZONES)
    allocated = allocate_resources(scored, total_medical, total_rescue)

    # Sort highest priority first for readability
    allocated.sort(key=lambda z: z["priority_score"], reverse=True)

    return jsonify(
        {
            "total_medical_teams": total_medical,
            "total_rescue_units": total_rescue,
            "zones": allocated,
        }
    )


if __name__ == "__main__":
    port = int(os.environ.get("APP_PORT", 5000))
    app.run(debug=True, port=port)
