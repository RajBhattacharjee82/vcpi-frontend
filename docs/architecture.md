# VCPI Frontend Architecture

## Layers
- UI pages under `src/pages` represent product tiers.
- Components under `src/components` keep presentational widgets reusable.
- API access under `src/api/client.py` isolates backend URL and request logic.

## Merge-ready decisions
- Keep all runtime code under `src` for easy movement into monorepo app folder.
- Keep endpoint names in one place (`src/api/client.py`) to reduce breakage.
- Keep environment config out of code via `.env`.

## Next frontend milestones
1. Render process graph from backend process-map endpoint.
2. Add variant drill-down charts with Plotly.
3. Add stateful live feed simulation for in-flight event updates.
4. Wire copilot panel to backend recommendation endpoint.
