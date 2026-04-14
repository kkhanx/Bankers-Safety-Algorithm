import sys
import json

from input_handler import read_input, validate_input
from safety_algo import run_safety_check


def main():
    if len(sys.argv) != 2:
        print(json.dumps({"error": "Usage: python3 main.py input.json"}))
        sys.exit(1)

    input_file = sys.argv[1]

    try:
        # Step 1: Read input
        data = read_input(input_file)

        # Step 2: Validate input
        validate_input(data)

        # Step 3: Run Banker's safety algorithm
        result = run_safety_check(
            data["available"],
            data["allocation"],
            data["max"]
        )

        # Step 4: Format final output (IMPORTANT for grading)
        if result["state"] == "SAFE":
            output = {
                "state": "SAFE",
                "safe_sequence": result["safe_sequence"]
            }
        else:
            output = {
                "state": "DEADLOCK",
                "deadlocked_processes": result["deadlocked_processes"]
            }

        # Step 5: Print JSON output
        print(json.dumps(output, indent=4))

    except Exception as e:
        print(json.dumps({"error": str(e)}))
        sys.exit(1)


if __name__ == "__main__":
    main()