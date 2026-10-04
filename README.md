# 🚀 D3 Autonomous Disaster Response Planner

---

## 👥 Team

| Field | Value |
|---|---|
| **Team Name** | Apex Squad |
| **Track** | AI |
| **Team Lead** | [Name] — [email@ibm.com] |
| **Members** | [Name 1], [Name 2], [Name 3] |

---

## 🎯 Problem Statement

During large-scale disasters, emergency coordinators must rapidly decide which zones need medical teams and rescue units first — with incomplete information and limited time. Poor allocation decisions cost lives. There is no lightweight, automated tool that scores zones by urgency and distributes limited resources proportionally.

---

## 💡 Solution

The **D3 Autonomous Disaster Response Planner** is a Python backend that ingests disaster zone data (severity, population, zone type, road accessibility), computes a priority score for each zone, and allocates a fixed pool of medical teams and rescue units proportionally across zones. It is exposed as both a REST API (Flask) and a CLI tool for instant use.

---

## ✨ Key Features

- **Priority Scoring Engine:** Calculates per-zone scores using severity × population × disaster-type multiplier × accessibility factor.
- **Proportional Allocation:** Distributes medical teams and rescue units across zones using floor-division with remainder top-up — no zone left with under-allocated rounding errors.
- **Flask REST API:** `GET /api/allocate` returns a fully scored and allocated JSON response for integration with any frontend or dashboard.
- **CLI Entry Point:** `python cli.py` prints a formatted allocation table to the console — no server needed for quick testing.
- **Environment-driven Configuration:** Total resource pools (`TOTAL_MEDICAL_TEAMS`, `TOTAL_RESCUE_UNITS`) are overridable via environment variables without code changes.

---

## 🛠️ Tech Stack

| Category | Technologies |
|---|---|
| **Languages** | Python 3.11+ |
| **Frameworks** | Flask |
| **IBM Technologies** | IBM Bob (used for planning and code generation) |
| **Databases** | None (hardcoded sample data — no DB dependency) |
| **Other** | GitHub Actions (CI validation) |

---

## 📁 Repository Structure

```
├── src/
│   └── backend/
│       ├── zones.py          # Sample disaster zone data
│       ├── scorer.py         # Priority score formula
│       ├── allocator.py      # Resource allocation logic
│       ├── app.py            # Flask API (GET /api/allocate, GET /health)
│       ├── cli.py            # CLI entry point
│       └── requirements.txt  # Python dependencies
├── docs/
│   ├── problem-statement.md
│   ├── solution-overview.md
│   ├── architecture.md
│   └── setup-guide.md
├── demo/
│   ├── screenshots/
│   └── demo-video-link.txt
├── presentation/
└── submission.yaml
```

---

## ⚡ How to Run

```bash
# 1. Clone the repo
git clone https://github.com/[your-org]/bob-ai-hackathon-Apex-squad.git
cd bob-ai-hackathon-Apex-squad/src/backend

# 2. Install dependencies
pip install -r requirements.txt

# 3. Configure environment (optional — defaults work out of the box)
cp .env.example .env

# 4a. Run via CLI
python cli.py

# 4b. Run the Flask API server
python app.py
# Then visit: http://127.0.0.1:5000/api/allocate
```

---

## 🖥️ Demo

| Artifact | Link |
|---|---|
| 📹 Demo Video | [See demo/demo-video-link.txt](demo/demo-video-link.txt) |
| 🌐 Live Demo | [See demo/live-demo-url.txt](demo/live-demo-url.txt) |
| 🖼️ Screenshots | [See demo/screenshots/](demo/screenshots/) |
| 📊 Presentation | [See presentation/](presentation/) |

---

## ⚠️ Known Limitations

- Zone data is hardcoded — no database or live data feed integration.
- The scoring formula uses fixed multipliers; weights are not yet tunable via config.
- Authentication is not implemented on the Flask routes (not production-ready).

---

## 🏅 What We're Most Proud Of

The allocation algorithm guarantees that the sum of allocated units always exactly equals the available pool (using proportional floor allocation with remainder top-up), and the clean separation between `scorer.py`, `allocator.py`, and `app.py` makes each layer independently testable and replaceable.
