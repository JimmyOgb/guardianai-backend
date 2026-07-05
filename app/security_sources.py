from app.integrations import (
    get_goplus,
    get_rugcheck,
    verify_contract,
)


# ----------------------------
# Main analyzer
# ----------------------------

async def analyze_token(
    token: str,
    chain: str,
    unlimited: bool,
):
    goplus = await get_goplus(
        "1",
        token,
    ) or {}

    rugcheck = await get_rugcheck(
        token,
    ) or {}

    verify = await verify_contract(
        token,
        chain,
    ) or {}

    print("GoPlus:", goplus)
    print("RugCheck:", rugcheck)
    print("Verify:", verify)

    return {
        "token_name": token,

        "contract_verified":
            verify.get(
                "verified",
                False,
            ),

        "owner_can_mint":
            goplus.get(
                "owner_can_mint",
                False,
            ),

        "liquidity_locked":
            rugcheck.get(
                "liquidity_locked",
                False,
            ),

        "unlimited_approval":
            unlimited,

        "upgradeable_proxy":
            verify.get(
                "proxy",
                False,
            ),

        "audit_available":
            False,

        "honeypot":
            goplus.get(
                "honeypot",
                False,
            ),

        "blacklisted":
            goplus.get(
                "blacklisted",
                False,
            ),

        "rug_score":
            rugcheck.get(
                "score",
                0,
            ),

        "simulation_risk":
            False,

        "gas_anomaly":
            False,
    }