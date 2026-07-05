import json
import subprocess


async def run_guardian(evidence):

    result = subprocess.run(
        [
            "node",
            "genlayer_client.js",
            json.dumps(evidence),
        ],
        capture_output=True,
        text=True,
    )

    print("STDOUT:", result.stdout)
    print("STDERR:", result.stderr)

    if result.returncode != 0:
        return {
            "success": False,
            "error": result.stderr,
        }

    return json.loads(
        result.stdout.strip()
    )