# HDD Scheduling Algorithm Simulation

This Python program simulates three common disk scheduling algorithms: First-Come, First-Served (FCFS), SCAN (Elevator Algorithm), and C-SCAN (Circular SCAN). It helps visualize and compare the head movement and total seek time for a given set of disk requests.

## Video Tutorial
https://github.com/user-attachments/assets/c8cab0b4-ee17-4acd-a8c1-547d1bae087a

## Implemented Algorithms

1. **First-Come, First-Served (FCFS)**: Processes requests in the order they arrive in the queue. Simple but can lead to high head movement.

2. **SCAN (Elevator Algorithm)**: The disk arm starts at one end of the disk and moves towards the other end, servicing requests along the way. When it reaches the other end, it reverses direction and continues servicing requests.

3. **C-SCAN (Circular SCAN)**: Similar to SCAN, but when the arm reaches the end, it immediately returns to the beginning of the disk without servicing any requests on the return trip. It then starts servicing requests from the beginning again.

## How to Run

1. Save the Python code as a `.py` file (e.g., `main.py`).

2. Open a terminal or command prompt.

3. Navigate to the directory where you saved the file.

4. Run the script using a Python interpreter:

```
python `main.py`
```

5. The program will prompt you to enter:

   - The total number of possible requests (used to generate random request numbers within the cylinder range).
   - The initial head position.
   - The total number of cylinders (e.g., 200 for cylinders 0-199).
   - The number corresponding to the algorithm you want to use (1 for FCFS, 2 for SCAN, 3 for C-SCAN).
   - If you choose SCAN, you will also be asked for the initial direction ('left' or 'right').

## Input

- `total_requests_possible`: An integer representing the range for generating random requests (0 to num_cylinders - 1).

- `initial_head_position`: An integer representing the starting position of the disk head.

- `num_cylinders`: An integer representing the total number of cylinders on the disk.

- `algorithm_choice`: An integer (1, 2, or 3) to select the algorithm.

- `scan_direction` (only for SCAN): A string ('left' or 'right') indicating the initial direction of head movement.

## Output

The program will output:

- The list of randomly generated requests.

- The sequence in which the requests are serviced by the chosen algorithm.

- The total seek time (which is equal to the total head movements in this simulation).

- The total number of head movements.

## Dependencies

This program uses standard Python libraries and does not require any external installations.

- `random`: Used for generating random disk requests.
