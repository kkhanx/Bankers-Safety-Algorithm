# COMP 3300 – Mini Project  
## Deadlock Detection using Banker's Safety Algorithm

### Team Members
- Mahnoz
- Yumna
- Kulsum
- Yusriyah
- Najiya

---

## Overview

This project implements the **Banker's Safety Algorithm** to determine whether a system is in a **safe state** or **deadlocked**.

The program:
- Reads system state from a JSON file
- Computes the **need matrix**
- Runs the **Banker's safety check**
- Outputs either:
  - A **safe sequence**, or
  - A list of **deadlocked processes**

---

## How It Works

Each process has:
- **Max** → maximum resources it may request
- **Allocation** → resources currently held
- **Need** → remaining resources needed (`Need = Max - Allocation`)

### Algorithm Steps

1. Start with the **available** resources
2. Find a process whose **need ≤ available**
3. Simulate the process finishing
4. Release its resources back to available
5. Repeat until:
   - All processes finish → **SAFE**
   - No process can proceed → **DEADLOCK**

---

## Tie-Breaking Policy

When multiple processes can proceed, the algorithm always selects the process with the **smallest index first** (e.g., P1 before P2).

This ensures deterministic output.

---

## Project Structure

```
.
├── input_handler.py
├── need_calculator.py
├── safety_algo.py
├── main.py
├── input.json
├── output.json
├── test_input_handler.py
└── README.md
```

---

## How to Run

### Basic run

```
python3 main.py input.json
```

### Required assignment format

```
python3 main.py input.json > output.json
```

---

## Input Format (JSON)

```json
{
  "processes": 3,
  "resources": 3,
  "available": [3, 3, 2],
  "max": [
    [7, 5, 3],
    [3, 2, 2],
    [9, 0, 2]
  ],
  "allocation": [
    [0, 1, 0],
    [2, 0, 0],
    [3, 0, 2]
  ]
}
```

---

## Output Format

### SAFE state

```json
{
  "state": "SAFE",
  "safe_sequence": ["P1", "P2", "P3"]
}
```

### DEADLOCK state

```json
{
  "state": "DEADLOCK",
  "deadlocked_processes": ["P1", "P3"]
}
```

---

## Design Decisions

- Modular structure separating input, computation, and algorithm
- Deterministic tie-breaking using smallest process index
- Input validation ensures correctness and prevents invalid states

---

## Testing

Test cases include:
- Safe scenarios
- Deadlock scenarios
- Tie-breaking cases
- Invalid input cases

---

## AI Usage Statement

AI tools (ChatGPT) were used to assist with:
- Understanding the Banker’s algorithm
- Structuring the project

All code was reviewed and understood before submission.

---

## Notes

- Output strictly follows required JSON format
- Process names are formatted as: P1, P2, ..., Pn