# Banker's safety algorithm: Determines whether the system is SAFE or in DEADLOCK using the need, allocation,
# and available resources.

# Tie-breaking rule:
# If multiple processes can run, choose the one with the smallest index first.

from need_calculator import calculate_need


# Check whether a process's need can be satisfied with the current work vector
def _need_leq_work(need_row, work):
    # Return True if need_row[j] <= work[j] for every resource j
    return all(need_row[j] <= work[j] for j in range(len(work)))

# Run the Banker's safety check 
def run_safety_check(available, allocation, max_matrix):

    # Returns:
        # SAFE result with safe_Sequence if all processes can finish
        # DEADLOCK result with deadlock_processes otherwise 

    # First compute the need matrix
    need_matrix = calculate_need(max_matrix, allocation)

    # Number of processes
    n = len(allocation)

    # Number of resource types
    m = len(available)

    # Work is a copy of availbale resources used during the simulation
    work = available[:]

    # finish[i] tells us whether process i has completed
    finish = [False] * n

    # Store the order in which processes safely complete
    safe_sequence = []

    # Keep trying to find a process that can finish 
    while True:
        chosen = None
        
        # Choose the first unfinished process whose need can be met
        # Since we loop from smallest index upward, tie-breaking is automatic
        for i in range(n):
            if not finish[i] and _need_leq_work(need_matrix[i], work):
                chosen = i
                break

        # If no process can proceed, stop the algorithm
        if chosen is None:
            break

        # Simulate the chosen process finishing 
        # When it finishes, it releases its alloated resources back to work 
        for j in range(m):
            work[j] += allocation[chosen][j]

        # Mark the process as finished
        finish[chosen] = True

        # Add the process name to the safe sequence
        safe_sequence.append(f"P{chosen + 1}")

    # If all processes finished, the system is in a safe state
    if all(finish):
        return {
            "state": "SAFE",
            "need_matrix": need_matrix,
            "safe_sequence": safe_sequence,
        }

    # Otherwise, any unfinished process is considered deadlocked
    deadlocked = [f"P{i + 1}" for i in range(n) if not finish[i]]
    return {
        "state": "DEADLOCK",
        "need_matrix": need_matrix,
        "deadlocked_processes": deadlocked,
    }
