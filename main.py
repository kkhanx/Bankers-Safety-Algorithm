import sys
import json
import re

from input_handler import read_input, validate_input
from safety_algo import run_safety_check

# Convert a python object to nicely formatted JSON 
# This version also collapses simple arrays onto one line for cleaner output
def pretty_json(obj):

    #First convert the object to indented JSON text
    text = json.dumps(obj, indent=2)

    #Helper function used by re.sub to collapse multi-line
    def collapse_array(match):

        # Get the inside content of the matched array 
        content = match.group(1)

        # Split the lines, clean whitespace, and remove trailing commas
        items = [item.strip().rstrip(',') for item in content.splitlines()]
        
        # Rebuild the array on one line
        return "[" + ", ".join(items) + "]"

    # Replace simple multi-line arrays with single-line versions
    return re.sub(r'\[\n([^\[\]]*?)\n\s*\]', collapse_array, text)

# Main driver function for the progam 
def main():

    # The program should be run with exactly one input file argument
    if len(sys.argv) != 2:
        print(json.dumps({"error": "Usage: python3 main.py input.json"}))
        sys.exit(1)

    # Get the input file name from the command line
    input_file = sys.argv[1]

    try:
        # Read input from JSON file
        data = read_input(input_file)

        # Validate input structure and values
        validate_input(data)

        # Run the safety algorithm
        result = run_safety_check(
            data["available"],
            data["allocation"],
            data["max"]
        )

        # Build the final output in the required JSON format
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

        # Print the final JSON output
        print(pretty_json(output))

    except Exception as e:
        #if any error happens, print it as JSON and exit with an error code
        print(json.dumps({"error": str(e)}))
        sys.exit(1)

#Run main() only when this file is executed directly
if __name__ == "__main__":
    main()
