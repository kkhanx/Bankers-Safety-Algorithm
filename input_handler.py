import json
#README
#hey teamates you can edit the values in input.json to test of the code
#like change the numbers to see when it deadlocks and
#when it is safe :)
#lmk if u find any errors in my code ok thx u

# adding comment

#hint: btw the output.json file will only be created if there are no errors 
#to run the code do --> python test_input_handler.py -->in the termila 
#contact me if u have question inshAllah

#function: rread and parse JSON 
def read_input(file_path):
    """reads and parses the JSON input file
    returns a dictionary of data
    """
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        raise Exception("Error: Input file not found.")
    except json.JSONDecodeError:
        raise Exception("Error: Invalid JSON format.")


#function: validate input data
def validate_input(data):
    """validates the structure and values of input JSON
    raises Exception if invalid
    """

    required_keys = ["processes", "resources", "available", "max", "allocation"]

    #check all required keys exist
    for key in required_keys:
        if key not in data:
            raise Exception(f"Error: Missing key '{key}' in input.")

    processes = data["processes"]
    resources = data["resources"]
    available = data["available"]
    max_matrix = data["max"]
    allocation = data["allocation"]

    #validate types
    if not isinstance(processes, int) or processes <= 0:
        raise Exception("Error: 'processes' must be a positive integer.")

    if not isinstance(resources, int) or resources <= 0:
        raise Exception("Error: 'resources' must be a positive integer.")

    #validate available vector
    if len(available) != resources:
        raise Exception("Error: 'available' length must match number of resources.")

    #validate matrices dimensions
    if len(max_matrix) != processes or len(allocation) != processes:
        raise Exception("Error: 'max' and 'allocation' must match number of processes.")

    for i in range(processes):
        if len(max_matrix[i]) != resources:
            raise Exception(f"Error: Row {i} of 'max' must have {resources} resources.")

        if len(allocation[i]) != resources:
            raise Exception(f"Error: Row {i} of 'allocation' must have {resources} resources.")

    #validate values (non-negative integers)
    for value in available:
        if value < 0:
            raise Exception("Error: 'available' cannot contain negative values.")

    for i in range(processes):
        for j in range(resources):
            if max_matrix[i][j] < 0 or allocation[i][j] < 0:
                raise Exception("Error: 'max' and 'allocation' cannot contain negative values.")

            if allocation[i][j] > max_matrix[i][j]:
                raise Exception(f"Error: allocation[{i}][{j}] cannot exceed max[{i}][{j}].")

    return True

#function: format process names
def format_processes(n):
    """returns list of process names: ["P1", "P2", ..., "Pn"]"""
    return [f"P{i+1}" for i in range(n)]

#function: write output JSON
def write_output(file_path, result):
    """writes result dictionary to JSON file in required format """
    try:
        with open(file_path, 'w') as file:
            json.dump(result, file, indent=4)
    except Exception as e:
        raise Exception(f"Error writing output: {str(e)}")