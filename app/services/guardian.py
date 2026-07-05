from app.security_sources import analyze_token
from app.genlayer import run_guardian


async def analyze_transaction(
    token_address: str,
    chain: str,
    unlimited_approval: bool,
):
    evidence = await analyze_token(
        token_address,
        chain,
        unlimited_approval,
    )

    print("EVIDENCE:", evidence)

    guardian = await run_guardian(evidence)

    print("GUARDIAN:", guardian)

    return {
        "success": True,
        "token": token_address,
        "security": evidence,
        "guardian": guardian,
    }