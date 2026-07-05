from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from app.services.guardian import analyze_transaction

app = FastAPI(
    title="Guardian AI Backend",
    version="1.0.0",
)

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        # Local development
        "http://localhost:5173",
        "http://localhost:5174",
        "http://127.0.0.1:5173",
        "http://127.0.0.1:5174",

        # Production frontend (Vercel)
        "https://guardian-ai-ybju-jm5avu8zl-jamism123.vercel.app",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class ScanRequest(BaseModel):
    token_address: str
    chain: str = "ethereum"
    unlimited_approval: bool = False


@app.get("/")
async def root():
    return {
        "status": "online",
        "service": "Guardian AI Backend",
    }


@app.post("/scan")
async def scan(request: ScanRequest):
    return await analyze_transaction(
        request.token_address,
        request.chain,
        request.unlimited_approval,
    )