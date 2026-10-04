# Solution Overview

## What We Built

The **D3 Autonomous Disaster Response Planner** is a Python backend that takes a set of disaster zones, scores each one by urgency, and allocates a fixed pool of medical teams and rescue units proportionally. It runs as a Flask REST API or as a standalone CLI tool.

## How It Works

1. **Zone data is loaded** from `zones.py` — each zone carries a severity rating (1–10), affected population, zone type (flood / earthquake / fire / other), and road accessibility.
2. **Priority scores are calculated** in `scorer.py` using the formula: `severity × population × type_multiplier × accessibility_factor`. Earthquakes receive the highest multiplier (1.5×); inaccessible roads reduce the score by 20%.
3. **Resources are allocated** in `allocator.py` — each zone receives a share of medical teams and rescue units proportional to its priority score. Floor division is used and any rounding remainder is awarded to the top-scoring zones so totals always add up exactly.
4. **Results are served** via `app.py` (Flask `GET /api/allocate` → JSON) or printed to the console via `cli.py`.

## Architecture Diagram

See [`architecture.md`](architecture.md) for the full Mermaid diagram.

```
[Operator]  →  cli.py  →  scorer.py  →  allocator.py  →  console table
[HTTP Client] → app.py → scorer.py  →  allocator.py  →  JSON response
                              ↑
                          zones.py (data)
```

## Key Design Decisions

| Decision | Rationale |
|---|---|
| Pure-function scorer and allocator | Makes each layer independently unit-testable; no side effects |
| Floor allocation with remainder top-up | Guarantees total allocated always equals total available — no rounding shortfall |
| Road inaccessibility reduces score (not increases) | Reflects actionable priority — hard-to-reach zones get fewer units until access is restored |
| No database | Simplifies the prototype; zone data source is a single swap-out point for production |
| Flask over FastAPI | Minimal dependency footprint; sufficient for a hackathon REST surface |

## IBM Technologies Used

- **IBM Bob:** Used as the AI planning and code-generation tool to design the architecture, write and validate all source files, and produce documentation for this submission.
