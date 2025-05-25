# Price Estimator

A web app to generate cost estimates from vendor price books (Excel/PDF on Google Drive), email estimates to clients, and export ServiceTitan-compatible files.

---

## Backend (FastAPI, SQLite, Google Drive, SendGrid)
- Located in `/backend/`
- Install dependencies: `pip install -r requirements.txt`
- Run: `uvicorn src.main:app --reload`
- Configure Google credentials and SendGrid API in `/backend/config/`
- Data ingestion and monthly update scripts included

## Frontend (Next.js + Tailwind CSS)
- Located in `/frontend/`
- Install dependencies: `npm install`
- Run locally: `npm run dev`
- Configure API URL in `.env.local` (for Vercel, set `NEXT_PUBLIC_API_URL`)
- Deploy to Vercel: Connect repo, import, and deploy

## MCP Automation
- MCP servers for Google Drive, SQLite, and SendGrid in `/mcp/`
- Configure in `mcp_config.json`

## Deployment
- Vercel: Uses `vercel.json` for backend API rewrites
- Heroku: Deploy FastAPI backend

## Testing
- Backend: `pytest` in `/backend/tests/`
- Frontend: Use Playwright or Cypress for E2E if desired

## To Do
- Add Google Drive OAuth credentials and vendor folder IDs
- Add SendGrid API key
- (Optional) Add authentication

## Contact
For issues or improvements, contact the project maintainer.
