# VCPI Frontend (Streamlit)

Frontend app for VC Process Intelligence Accelerator.

## Why this structure is merge-friendly
- API access is centralized in `src/api/client.py`.
- Page modules map directly to product capabilities (discovery, diagnostics, monitoring, copilot).
- This folder can move into a monorepo location like `apps/frontend` without code churn.

## Project layout
- `src/app.py` landing page
- `src/pages` Streamlit multi-page app views
- `src/api` backend client wrappers
- `src/components` reusable widgets
- `src/types` shared frontend contracts
- `docs` architecture and contribution notes

## Quick start

```powershell
./scripts/bootstrap.ps1
./scripts/run.ps1
```

Manual:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
copy .env.example .env
streamlit run src/app.py
```

## GitHub repo setup

```powershell
git init
git add .
git commit -m "Initial Streamlit frontend scaffold"
```
