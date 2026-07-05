from pydantic import BaseModel


class TransactionRequest(
    BaseModel,
):
    token_address: str
    chain: str
    unlimited_approval: bool


class SecurityEvidence(
    BaseModel,
):
    token_name: str
    contract_verified: bool
    owner_can_mint: bool
    liquidity_locked: bool
    unlimited_approval: bool
    upgradeable_proxy: bool
    audit_available: bool
    honeypot: bool
    blacklisted: bool
    rug_score: int
    simulation_risk: bool
    gas_anomaly: bool