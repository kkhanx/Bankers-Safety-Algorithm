from input_handler import read_input, validate_input, write_output
from safety_algo import run_safety_check


def test_all():
    print("- TESTING INPUT HANDLER -")

    #read input and print out the data in input.json
    data = read_input("input.json")
    print("Read Input:", data)

    #validate input
    try:
        validate_input(data)
        print("Validation: PASSED")
    except Exception as e:
        print("Validation: FAILED", e)
        return

    raw = run_safety_check(
        data["available"],
        data["allocation"],
        data["max"],
    )
    if raw["state"] == "SAFE":
        result = {
            "state": "SAFE",
            "safe_sequence": raw["safe_sequence"],
        }
    else:
        result = {
            "state": "DEADLOCK",
            "deadlocked_processes": raw["deadlocked_processes"],
        }

    write_output("output.json", result)
    print("Output written to output.json: \n", result)

if __name__ == "__main__":
    test_all()