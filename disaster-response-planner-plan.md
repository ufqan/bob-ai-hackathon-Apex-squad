# D3 Autonomous Disaster Response Planner — Backend Plan

## Overview

Build a small Python backend for the **D3 Autonomous Disaster Response Planner** that:
1. Holds a set of sample disaster zones (hardcoded).
2. Calculates a numeric priority score for each zone from four inputs: severity, population, zone type, and road accessibility.
3. Allocates a fixed pool of medical teams and rescue units proportionally across zones based on their scores.
4. Exposes the logic through two surfaces: a **Flask HTTP route** (JSON response) and a **CLI entry point** (console print).

All source code lives under `src/backend/`.

---

## Sub-Task 1 — Project Scaffold

**Intent**
Create the directory layout and dependency manifest so the project is runnable from a clean checkout.

**Expected Outcomes**
- `src/backend/` directory exists with an `__init__.py`.
- `src/backend/requirements.txt` lists `flask` (and nothing else — no heavy ML deps needed).
- `src/backend/.env.example` documents `TOTAL_MEDICAL_TEAMS` and `TOTAL_RESCUE_UNITS` config vars with sensible defaults (10 and 8).

**Todo List**
- [ ] Create `src/backend/__init__.py` (empty).
- [ ] Create `src/backend/requirements.txt` with `flask`.
- [ ] Create `src/backend/.env.example` with `TOTAL_MEDICAL_TEAMS=10` and `TOTAL_RESCUE_UNITS=8`.

**Relevant Context**
- `src/README.md` describes the `src/backend/` convention for web/API projects.
- `src/.env.example` is the root-level template — mirror its style.

**Status** `[ ] pending`

---

## Sub-Task 2 — Sample Zone Data Module

**Intent**
Define the hardcoded sample zones in one place so both the scorer and Flask route import from a single source of truth.

**Expected Outcomes**
- `src/backend/zones.py` exports a `SAMPLE_ZONES` list of dicts.
- Each zone dict has these keys: `id`, `name`, `severity` (1–10 int), `population` (int), `zone_type` (`"flood"` | `"earthquake"` | `"fire"` | `"other"`), `road_accessible` (bool).
- At least 4 sample zones covering different types and accessibilities are included.

**Todo List**
- [ ] Create `src/backend/zones.py`.
- [ ] Define `SAMPLE_ZONES` with ≥ 4 representative zones spanning all four `zone_type` values.

**Relevant Context**
- Inputs confirmed by user: severity, population, zone_type, road_accessible.
- This module has no dependencies — it is pure data.

**Status** `[ ] pending`

---

## Sub-Task 3 — Priority Scoring Engine

**Intent**
Implement the scoring formula in an isolated, testable module with no Flask dependency.

**Expected Outcomes**
- `src/backend/scorer.py` exports a `calculate_priority_score(zone: dict) -> float` function.
- `scorer.py` also exports `score_all_zones(zones: list) -> list` which returns the input list enriched with a `"priority_score"` key on each dict.
- The scoring formula uses:
  - **Base score** = `severity × population`
  - **Zone-type multiplier**: `earthquake` → 1.5, `flood` → 1.3, `fire` → 1.2, `other` → 1.0
  - **Accessibility penalty**: if `road_accessible` is `False`, multiply by 0.8 (harder to reach = slightly lower actionable priority)
- No external libraries needed beyond the Python standard library.

**Todo List**
- [ ] Create `src/backend/scorer.py`.
- [ ] Implement `calculate_priority_score(zone)` with the formula above.
- [ ] Implement `score_all_zones(zones)` that maps `calculate_priority_score` over the list.

**Relevant Context**
- Formula weights confirmed with user: severity × population × type_multiplier × accessibility_factor.
- Road accessibility reduces score (not increases) because inaccessible zones are harder to reach — a deliberate trade-off.

**Status** `[ ] pending`

---

## Sub-Task 4 — Resource Allocator

**Intent**
Implement allocation logic that converts scores into concrete unit counts for each zone.

**Expected Outcomes**
- `src/backend/allocator.py` exports `allocate_resources(scored_zones: list, total_medical: int, total_rescue: int) -> list`.
- Each element in the returned list contains the original zone fields plus `"priority_score"`, `"medical_teams_allocated"`, and `"rescue_units_allocated"`.
- Allocation formula: each zone receives `floor(score_fraction × total_units)` units; any remainder from floor-rounding is assigned to the highest-scoring zone.
- If `total_score` is zero (edge case), all allocations are zero.

**Todo List**
- [ ] Create `src/backend/allocator.py`.
- [ ] Implement `allocate_resources` using proportional floor allocation with remainder top-up.

**Relevant Context**
- Allocation is purely proportional to priority score — confirmed by user.
- `math.floor` from the standard library is sufficient; no numpy/scipy needed.

**Status** `[ ] pending`

---

## Sub-Task 5 — Flask App and API Route

**Intent**
Wrap the scorer and allocator behind a single Flask endpoint so the system can be called over HTTP and returns JSON.

**Expected Outcomes**
- `src/backend/app.py` creates a Flask application.
- `GET /api/allocate` runs the full pipeline (score → allocate) on `SAMPLE_ZONES` and returns a JSON body:
  ```
  {
    "total_medical_teams": 10,
    "total_rescue_units": 8,
    "zones": [ { ...zone fields, priority_score, medical_teams_allocated, rescue_units_allocated }, ... ]
  }
  ```
- `TOTAL_MEDICAL_TEAMS` and `TOTAL_RESCUE_UNITS` are read from environment variables (with defaults 10 and 8).
- `GET /health` returns `{"status": "ok"}` for liveness checks.
- Running `python app.py` starts the dev server on port 5000.

**Todo List**
- [ ] Create `src/backend/app.py` with Flask app, `/api/allocate` route, and `/health` route.
- [ ] Read resource totals from `os.environ` with `int(os.environ.get(..., default))`.

**Relevant Context**
- `src/.env.example` already patterns `APP_PORT=8000`; follow the same style for the two new vars.
- Flask is the only framework dependency.

**Status** `[ ] pending`

---

## Sub-Task 6 — CLI Entry Point

**Intent**
Provide a standalone script that runs the full pipeline and prints results to the console — useful for quick testing without starting a server.

**Expected Outcomes**
- `src/backend/cli.py` is a runnable script (`python cli.py`).
- It imports `SAMPLE_ZONES`, `score_all_zones`, and `allocate_resources`.
- It prints a formatted table to stdout: one row per zone showing name, score, medical teams, rescue units.
- No Flask dependency — pure Python.

**Todo List**
- [ ] Create `src/backend/cli.py` with a `main()` function guarded by `if __name__ == "__main__"`.
- [ ] Format output as a simple columnar table using `str.format()` or `f-strings` (no external table libs).

**Relevant Context**
- User confirmed CLI output should go to the console; JSON output is reserved for the Flask route.
- `cli.py` must not import from `app.py` to avoid pulling in Flask as a dependency for CLI-only runs.

**Status** `[ ] pending`

---

## File Map

```
src/
└── backend/
    ├── __init__.py          ← empty package marker
    ├── requirements.txt     ← flask only
    ├── .env.example         ← TOTAL_MEDICAL_TEAMS, TOTAL_RESCUE_UNITS
    ├── zones.py             ← SAMPLE_ZONES list
    ├── scorer.py            ← calculate_priority_score, score_all_zones
    ├── allocator.py         ← allocate_resources
    ├── app.py               ← Flask app, /api/allocate, /health
    └── cli.py               ← CLI entry point
```

---

## Open Decisions / Constraints

| Decision | Chosen Approach |
|---|---|
| Score formula | severity × population × type_multiplier × accessibility_factor |
| Type multipliers | earthquake 1.5 · flood 1.3 · fire 1.2 · other 1.0 |
| Accessibility factor | road_accessible=False → 0.8 |
| Allocation | Proportional floor with remainder to top scorer |
| Data source | Hardcoded SAMPLE_ZONES — no DB, no file I/O |
| Flask version | Latest stable (no version pin needed for hackathon) |
