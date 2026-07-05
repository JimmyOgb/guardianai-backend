import httpx


async def get_rugcheck(
    token: str
):

    url = (
        "https://api.rugcheck.xyz/v1/"
        f"tokens/{token}/report"
    )

    try:

        async with httpx.AsyncClient(
            timeout=20
        ) as client:

            response = await client.get(
                url
            )

        if response.status_code != 200:
            return None

        data = response.json()

        return {
            "score":
                data.get(
                    "score",
                    0
                ),

            "liquidity_locked":
                data.get(
                    "liquidityLocked",
                    False
                ),

            "warnings":
                data.get(
                    "warnings",
                    []
                ),
        }

    except Exception:

        return {
            "score": 0,
            "liquidity_locked": False,
            "warnings": [],
        }