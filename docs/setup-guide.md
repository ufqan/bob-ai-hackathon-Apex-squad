# Setup Guide

> **This file is read by the automated evaluation pipeline. Be precise and complete.**

## Prerequisites

Before you begin, ensure you have the following installed:

- [x] Python 3.9 or higher (`python --version`)
- [x] pip (`pip --version`)

No database, no Docker, no cloud account required.

## Environment Variables

All environment variables have safe defaults and the application works out of the box without a `.env` file. To customise:

```bash
cd src/backend
cp .env.example .env
# Edit .env as needed
```

| Variable | Description | Default |
|---|---|---|
| `TOTAL_MEDICAL_TEAMS` | Total medical teams available for allocation | `10` |
| `TOTAL_RESCUE_UNITS` | Total rescue units available for allocation | `8` |
| `APP_PORT` | Port the Flask server binds to | `5000` |
| `APP_ENV` | `development` or `production` | `development` |

## Installation

```bash
# 1. Clone the repository
git clone https://github.com/[your-org]/bob-ai-hackathon-Apex-squad.git

# 2. Navigate to the backend source directory
cd bob-ai-hackathon-Apex-squad/src/backend

# 3. Install Python dependencies
pip install -r requirements.txt
```

## Running the Application

### Option A — CLI (no server, instant output)

```bash
cd src/backend
python cli.py
```

Expected output: a formatted table showing each disaster zone, its priority score, and the number of medical teams and rescue units allocated.

### Option B — Flask REST API

```bash
cd src/backend
python app.py
```

The server starts on `http://127.0.0.1:5000`.

Available endpoints:

| Endpoint | Method | Description |
|---|---|---|
| `/api/allocate` | GET | Returns scored zones and resource allocations as JSON |
| `/health` | GET | Liveness check — returns `{"status": "ok"}` |

Example request:
```bash
curl http://127.0.0.1:5000/api/allocate
```

### Overriding resource totals at runtime

```bash
# Linux / macOS
TOTAL_MEDICAL_TEAMS=20 TOTAL_RESCUE_UNITS=15 python cli.py

# Windows PowerShell
$env:TOTAL_MEDICAL_TEAMS=20; $env:TOTAL_RESCUE_UNITS=15; python cli.py
```

## Running Tests

No automated test suite is included in this prototype. To manually verify correctness, run:

```bash
python cli.py
```

The output totals row must show `TOTALS` summing to exactly `TOTAL_MEDICAL_TEAMS` and `TOTAL_RESCUE_UNITS`.

## Troubleshooting

| Issue | Solution |
|---|---|
| `ModuleNotFoundError: No module named 'flask'` | Run `pip install -r requirements.txt` from `src/backend/` |
| `Address already in use` on port 5000 | Set `APP_PORT=5001` in `.env` or run `python app.py` after killing the existing process |
| `python` not found | Ensure Python 3.9+ is on your `PATH`; try `python3 cli.py` on Linux/macOS |
