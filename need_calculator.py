def calculate_need(max_matrix, allocation):
    """calculates the need matrix based on max and allocation matrices
    returns the need matrix
    """

    processes = len(max_matrix)
    resources = len(max_matrix[0])
    need_matrix = [[0] * resources for _ in range(processes)]

    for i in range(processes):
        for j in range(resources):
            #need = max - allocation (remaining resources needed)
            need_matrix[i][j] = max_matrix[i][j] - allocation[i][j]

    return need_matrix