import "dotenv/config";

import {
  createClient,
  createAccount,
} from "genlayer-js";

import {
  studionet,
} from "genlayer-js/chains";

const CONTRACT =
  process.env.GENLAYER_CONTRACT;

const PRIVATE_KEY =
  process.env.GENLAYER_PRIVATE_KEY;

const account =
  createAccount(PRIVATE_KEY);

const client =
  createClient({
    chain: studionet,
    account,
  });

async function run() {
  try {

    const evidence =
      JSON.parse(
        process.argv[2]
      );

    // Debug goes to stderr
    console.error(
      "Submitting transaction..."
    );

    const hash =
      await client.writeContract({
        address: CONTRACT,
        functionName:
          "analyze_transaction",
        args: [
          evidence.token_name,
          evidence.contract_verified,
          evidence.owner_can_mint,
          evidence.liquidity_locked,
          evidence.unlimited_approval,
          evidence.upgradeable_proxy,
          evidence.audit_available,
          evidence.honeypot,
          evidence.blacklisted,
          evidence.rug_score,
          evidence.simulation_risk,
          evidence.gas_anomaly,
        ],
      });

    console.error(
      "TX:",
      hash
    );

    const receipt =
      await client.waitForTransactionReceipt({
        hash,
      });

    // ONLY JSON goes to stdout
    console.log(
      JSON.stringify({
        success: true,
        txHash: receipt.hash,
        status: receipt.status_name,
        consensus:
          receipt.result_name,
        contract:
          CONTRACT,
        sender:
          receipt.sender,
      })
    );

  } catch (err) {

    // Errors also go to stderr
    console.error(
      JSON.stringify({
        success: false,
        error:
          err.message,
        stack:
          err.stack,
      })
    );

    process.exit(1);
  }
}

run();