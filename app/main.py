from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from app.services.guardian import analyze_transaction

app = FastAPI(
    title="Guardian AI Backend",
    version="1.0.0",
)

# Hackathon/demo CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
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
        "version": "1.0.0",
    }


@app.get("/health")
async def health():
    return {
        "status": "healthy",
    }


@app.post("/scan")
async def scan(request: ScanRequest):
    return await analyze_transaction(
        request.token_address,
        request.chain,
        request.unlimited_approval,
    )