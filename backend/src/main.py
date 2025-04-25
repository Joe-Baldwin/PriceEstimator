import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import json
from src.data_ingestion.sqlite_storage import init_db
from src.api.routes import router as api_router

# Load environment variables
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '../config/.env'))

app = FastAPI()

# Allow frontend (React) to connect
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize SQLite DB
init_db()

@app.get("/vendors")
def get_vendors():
    vendor_mapping_path = os.path.join(os.path.dirname(__file__), '../config/vendor_mapping.json')
    with open(vendor_mapping_path, 'r') as f:
        data = json.load(f)
    return [{"id": v["id"], "name": v["name"]} for v in data["vendors"]]

# Include API router
app.include_router(api_router)
