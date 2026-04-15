# Calculate the need matrix using: 
# need = max - allocation

def calculate_need(max_matrix, allocation):
    """calculates and return the need matrix"""

    # Number of processes = number of rows in the matrix
    processes = len(max_matrix)

    # Number of resource types = number of colums in each row
    resources = len(max_matrix[0])

    # Create an empty need matrix filled with 0s
    need_matrix = [[0] * resources for _ in range(processes)]

    # Compute the remaining resources needed for each process
    for i in range(processes):
        for j in range(resources):
            #need = max - allocation (remaining resources needed)
            need_matrix[i][j] = max_matrix[i][j] - allocation[i][j]

    return need_matrix