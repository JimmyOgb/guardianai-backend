def submit_guardian_transaction(
    security_data,
):
    return {
        "success": True,
        "txHash": "wallet-signing-pending",
        "status": "ANALYZED",
        "consensus": "CLIENT_SIDE_SIGNATURE",
        "contract": "MetaMask",
        "sender": "User Wallet",
    }