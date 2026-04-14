"""Banker's safety algorithm: safe sequence or deadlocked processes.

Tie-breaking when multiple processes can proceed: smallest process index first.
"""

from need_calculator import calculate_need


def _need_leq_work(need_row, work):
    """Return True if need_row[j] <= work[j] for every resource j."""
    return all(need_row[j] <= work[j] for j in range(len(work)))


def run_safety_check(available, allocation, max_matrix):
    """
    Run the Banker's safety algorithm.

    Parameters
    ----------
    available : list[int]
        Available resource vector (length = resources).
    allocation : list[list[int]]
        Current allocation matrix (processes x resources).
    max_matrix : list[list[int]]
        Maximum demand matrix (same shape as allocation).

    Returns
    -------
    dict
        If safe:
            {"state": "SAFE", "need_matrix": [...], "safe_sequence": ["P1", ...]}
        If unsafe (deadlock / no safe sequence from this state):
            {"state": "DEADLOCK", "need_matrix": [...],
             "deadlocked_processes": ["P2", ...]}  # processes that cannot finish
    """
    need_matrix = calculate_need(max_matrix, allocation)
    n = len(allocation)
    m = len(available)

    work = available[:]
    finish = [False] * n
    safe_sequence = []

    while True:
        chosen = None
        # Smallest process index first among those that can run
        for i in range(n):
            if not finish[i] and _need_leq_work(need_matrix[i], work):
                chosen = i
                break

        if chosen is None:
            break

        # Simulate P_chosen completing: release its allocation
        for j in range(m):
            work[j] += allocation[chosen][j]
        finish[chosen] = True
        safe_sequence.append(f"P{chosen + 1}")

    if all(finish):
        return {
            "state": "SAFE",
            "need_matrix": need_matrix,
            "safe_sequence": safe_sequence,
        }

    deadlocked = [f"P{i + 1}" for i in range(n) if not finish[i]]
    return {
        "state": "DEADLOCK",
        "need_matrix": need_matrix,
        "deadlocked_processes": deadlocked,
    }
