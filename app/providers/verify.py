import os
import httpx


async def verify_contract(
    address: str,
    chain: str = "ethereum"
):

    if chain == "base":
        endpoint = "https://api.basescan.org/api"
        key = os.getenv("BASESCAN_API_KEY")
    else:
        endpoint = "https://api.etherscan.io/api"
        key = os.getenv("ETHERSCAN_API_KEY")

    params = {
        "module": "contract",
        "action": "getsourcecode",
        "address": address,
        "apikey": key,
    }

    async with httpx.AsyncClient(
        timeout=20
    ) as client:
        response = await client.get(
            endpoint,
            params=params,
        )

    data = response.json()

    if (
        "result" not in data
        or not data["result"]
    ):
        return {
            "verified": False,
            "proxy": False,
        }

    result = data["result"][0]

    return {
        "verified":
            bool(
                result.get(
                    "SourceCode",
                    ""
                )
            ),

        "proxy":
            result.get(
                "Proxy",
                "0"
            ) == "1",
    }