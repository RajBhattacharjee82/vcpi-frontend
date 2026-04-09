# Merge Strategy (Future Monorepo)

## Target path after merge
- Move this frontend repo into `apps/frontend`

## Current contract dependency
- Backend API contract mirror: `docs/api-contract.yaml`
- Environment variable: `BACKEND_BASE_URL`

## Contributor guardrails
1. Add new endpoint usage only through `src/api/client.py`.
2. Keep page files thin and put reusable UI in `src/components`.
3. Keep import paths relative to `src` package layout.
4. Avoid backend-only assumptions in frontend business logic.
