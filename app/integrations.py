import os
import httpx


ETHERSCAN_API_KEY = os.getenv(
    "ETHERSCAN_API_KEY"
)


async def get_goplus(
    chain_id: str,
    token: str,
):
    try:
        url = (
            "https://api.gopluslabs.io/"
            f"api/v1/token_security/"
            f"{chain_id}"
            f"?contract_addresses={token}"
        )

        async with httpx.AsyncClient(
            timeout=10,
        ) as client:
            r = await client.get(url)

        data = r.json()

        result = (
            data.get(
                "result",
                {},
            ).get(
                token.lower(),
                {},
            )
        )

        return {
            "owner_can_mint":
                result.get(
                    "owner_mintable",
                    "0",
                ) == "1",

            "honeypot":
                result.get(
                    "is_honeypot",
                    "0",
                ) == "1",

            "blacklisted":
                result.get(
                    "is_blacklisted",
                    "0",
                ) == "1",
        }

    except Exception as e:
        print(
            "GoPlus error:",
            e,
        )

        return {
            "owner_can_mint": False,
            "honeypot": False,
            "blacklisted": False,
        }


async def get_rugcheck(
    token: str,
):
    try:
        url = (
            "https://api.rugcheck.xyz/"
            f"v1/tokens/{token}"
        )

        async with httpx.AsyncClient(
            timeout=10,
        ) as client:
            r = await client.get(url)

        if r.status_code != 200:
            return {
                "liquidity_locked": False,
                "score": 0,
            }

        data = r.json()

        return {
            "liquidity_locked":
                data.get(
                    "liquidity_locked",
                    False,
                ),

            "score":
                data.get(
                    "rug_score",
                    0,
                ),
        }

    except Exception as e:
        print(
            "RugCheck error:",
            e,
        )

        return {
            "liquidity_locked": False,
            "score": 0,
        }


async def verify_contract(
    token: str,
    chain: str,
):
    try:

        if chain != "ethereum":
            return {
                "verified": False,
                "proxy": False,
            }

        url = (
            "https://api.etherscan.io/api"
            "?module=contract"
            "&action=getsourcecode"
            f"&address={token}"
            f"&apikey={ETHERSCAN_API_KEY}"
        )

        async with httpx.AsyncClient(
            timeout=10,
        ) as client:
            r = await client.get(url)

        data = r.json()

        result = (
            data.get(
                "result",
                [{}],
            )[0]
        )

        return {
            "verified":
                bool(
                    result.get(
                        "SourceCode",
                        "",
                    )
                ),

            "proxy":
                bool(
                    result.get(
                        "Proxy",
                        "0",
                    ) == "1"
                ),
        }

    except Exception as e:
        print(
            "Verify error:",
            e,
        )

        return {
            "verified": False,
            "proxy": False,
        }