import { createClient } from "genlayer-js";
import { studionet } from "genlayer-js/chains";

console.log("Studionet RPC:");
console.log(studionet.rpcUrls);

const client = createClient({
  chain: studionet,
});

try {
  console.log("Connecting...");

  const block =
    await client.getBlockNumber();

  console.log(
    "Connected!"
  );

  console.log(
    "Latest block:",
    block
  );

} catch (err) {

  console.error(
    "RPC ERROR:"
  );

  console.error(err);
}