import httpx


async def get_goplus(chain_id: str, token: str):

    url = (
        f"https://api.gopluslabs.io/api/v1/"
        f"token_security/{chain_id}"
        f"?contract_addresses={token}"
    )

    async with httpx.AsyncClient(timeout=20) as client:
        response = await client.get(url)

    data = response.json()

    if (
        "result" not in data
        or token.lower() not in data["result"]
    ):
        return {
            "owner_can_mint": False,
            "honeypot": False,
            "blacklisted": False,
            "proxy": False,
            "open_source": False,
        }

    token_data = data["result"][token.lower()]

    return {
        "owner_can_mint":
            token_data.get(
                "is_mintable",
                "0"
            ) == "1",

        "honeypot":
            token_data.get(
                "is_honeypot",
                "0"
            ) == "1",

        "blacklisted":
            token_data.get(
                "is_blacklisted",
                "0"
            ) == "1",

        "proxy":
            token_data.get(
                "is_proxy",
                "0"
            ) == "1",

        "open_source":
            token_data.get(
                "is_open_source",
                "0"
            ) == "1",
    }