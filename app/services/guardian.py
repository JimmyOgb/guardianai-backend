from app.genlayer import submit_guardian_transaction


async def analyze_transaction(
    token_address,
    chain,
    unlimited_approval=False,
):
    security = {
        "token_name": token_address,
        "contract_verified": True,
        "liquidity_locked": True,
        "honeypot": False,
        "rug_score": 2,
    }

    guardian = submit_guardian_transaction(
        security
    )

    return {
        "security": security,
        "guardian": guardian,
    }