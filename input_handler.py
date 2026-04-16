import json

# Read the input JSON file and convert it into a Python dictionary
def read_input(file_path):
    
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        raise Exception("Error: Input file not found.")
    except json.JSONDecodeError:
        raise Exception("Error: Invalid JSON format.")


# Check that the input data has the required structure and valid values
def validate_input(data):
    
    required_keys = ["processes", "resources", "available", "max", "allocation"]

    # Make sure all required keys exist in the JSON input
    for key in required_keys:
        if key not in data:
            raise Exception(f"Error: Missing key '{key}' in input.")

    # Extract values from the input dictionary
    processes = data["processes"]
    resources = data["resources"]
    available = data["available"]
    max_matrix = data["max"]
    allocation = data["allocation"]

    # Check that the number of processes is a positive integer
    if not isinstance(processes, int) or processes <= 0:
        raise Exception("Error: 'processes' must be a positive integer.")

    #Check that the number of resource types is a positive integer
    if not isinstance(resources, int) or resources <= 0:
        raise Exception("Error: 'resources' must be a positive integer.")

    # Check that the available vector matches the number of resources
    if len(available) != resources:
        raise Exception("Error: 'available' length must match number of resources.")

    # Check that max and allocation have the correct number of the process rows
    if len(max_matrix) != processes or len(allocation) != processes:
        raise Exception("Error: 'max' and 'allocation' must match number of processes.")

    # Check that each row in both matrices has the correct number of resource columns
    for i in range(processes):
        if len(max_matrix[i]) != resources:
            raise Exception(f"Error: Row {i} of 'max' must have {resources} resources.")

        if len(allocation[i]) != resources:
            raise Exception(f"Error: Row {i} of 'allocation' must have {resources} resources.")

    # Check that available resources are not negative
    for value in available:
        if value < 0:
            raise Exception("Error: 'available' cannot contain negative values.")

    # Check that max/allocation values are valid
    for i in range(processes):
        for j in range(resources):
            # Ensure resource values are not be negative
            if max_matrix[i][j] < 0 or allocation[i][j] < 0:
                raise Exception("Error: 'max' and 'allocation' cannot contain negative values.")

            # A process cannot already hold more than its declared maximum
            if allocation[i][j] > max_matrix[i][j]:
                raise Exception(f"Error: allocation[{i}][{j}] cannot exceed max[{i}][{j}].")

    return True

# Create process names in the format P1, P2, P3, ...
def format_processes(n):
    """returns list of process names: ["P1", "P2", ..., "Pn"]"""
    return [f"P{i+1}" for i in range(n)]

# Write the result dictionary to an output JSON file
def write_output(file_path, result):
    """writes result dictionary to JSON file in required format """
    try:
        with open(file_path, 'w') as file:
            json.dump(result, file, indent=4)
    except Exception as e:
        raise Exception(f"Error writing output: {str(e)}")