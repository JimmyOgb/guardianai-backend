from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from app.services.guardian import analyze_transaction

app = FastAPI()

# ✅ FIX: CORS (this solves OPTIONS 405 error)
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://localhost:5174",
        "http://127.0.0.1:5173",
        "http://127.0.0.1:5174",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class ScanRequest(BaseModel):
    token_address: str
    chain: str = "ethereum"
    unlimited_approval: bool = False


@app.post("/scan")
async def scan(request: ScanRequest):
    return await analyze_transaction(
        request.token_address,
        request.chain,
        request.unlimited_approval,
    )