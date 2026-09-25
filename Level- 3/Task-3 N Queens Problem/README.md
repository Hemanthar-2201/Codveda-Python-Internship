# N-Queens Problem Solver

## Description

This project is a Python implementation of the classic **N-Queens Problem** using a backtracking algorithm.

The objective of the N-Queens Problem is to place N queens on an N × N chessboard such that no two queens can attack each other.

The program represents the chessboard as a 2D array and uses backtracking to find a valid arrangement of queens.

## Features

- Accepts the number of queens from the user
- Represents the chessboard using a 2D list
- Places queens one row at a time
- Checks whether a position is safe before placing a queen
- Checks for conflicts in the same column
- Checks for conflicts on the upper-left diagonal
- Checks for conflicts on the upper-right diagonal
- Uses recursion and backtracking to find a solution
- Displays the solved chessboard
- Handles cases where no solution exists
- Handles invalid user input

## How the N-Queens Problem Works

A queen in chess can attack another queen if they are located in the same:

- Row
- Column
- Diagonal

The program places one queen in each row and checks whether the selected position is safe.

If a safe position is found, the queen is placed and the program moves to the next row.

If no safe position is available in a later row, the program backtracks by removing the previously placed queen and tries another position.

## Backtracking Approach

The program follows these steps:

```text
Start
  ↓
Create an empty N × N chessboard
  ↓
Start from the first row
  ↓
Try each column
  ↓
Is the position safe?
  ↓
 ┌───────────────┐
 │               │
Yes              No
 │               │
 ↓               ↓
Place queen    Try next column
 │
 ↓
Move to next row
 │
 ↓
Can all queens be placed?
 │
 ├── Yes → Display solution
 │
 └── No → Remove queen
             ↓
        Try another position
```

## Board Representation

The chessboard is represented using a 2D list.
For example, a 4 × 4 board initially looks like:

```text
. . . .
. . . .
. . . .
. . . .
```

Where:
- `Q` represents a queen
- `.` represents an empty position

A possible solution is:

```text
. . Q .
Q . . .
. . . Q
. Q . .
```

## Safety Checking

Before placing a queen, the program checks:

- **Same Column**: The program checks whether another queen already exists in the same column.
- **Upper-Left Diagonal**: The program checks the diagonal moving toward the upper-left direction.
- **Upper-Right Diagonal**: The program checks the diagonal moving toward the upper-right direction.

If a queen is found in any of these positions, the current position is considered unsafe.

## Backtracking

Backtracking is used when the current placement of queens does not lead to a complete solution.
The program:

1. Places a queen in a safe position.
2. Moves to the next row.
3. Continues placing queens.
4. If it reaches a situation where no safe position is available, it removes the previously placed queen.
5. It then tries another position.

This continues until a valid solution is found or all possibilities are exhausted.

## Special Cases

The N-Queens problem has no solution for:
- `N = 2`
- `N = 3`

A solution exists for:
- `N = 1`
- `N = 4`
- `N = 5`
- `N = 6`
- ...

For example, when `N = 4`, the program can find a valid arrangement of four queens.

## How to Run

### 1. Install Python
Make sure Python 3 is installed on your computer.

### 2. Open the Project Folder
Open the folder containing:
`n queees.py`

### 3. Run the Program
Open a terminal in the project folder and run:

```bash
python "n queees.py"
```

### 4. Enter the Number of Queens
The program will ask:

```text
Enter the number of queens:
```

For example:
`4`

The program will then search for a valid solution.

## Example Output

```text
---------- N-QUEENS SOLVER ----------

Enter the number of queens: 4

Solution found!

---------- CHESSBOARD ----------
. . Q .
Q . . .
. . . Q
. Q . .
________________________________
```

If no solution exists:

```text
Enter the number of queens: 3

No solution exists for 3 queens.
```

## Error Handling

The application handles:
- Non-numeric input
- Numbers less than 1
- N values for which no solution exists

For example:

```text
Enter the number of queens: abc

Invalid input. Please enter a whole number.
```

## Technologies Used

- Python 3
- 2D Lists
- Recursion
- Backtracking
- Conditional Statements
- Loops
- Functions
- Command-Line Interface
- Exception Handling

## What I Learned

Through this project, I practiced:

- Working with 2D lists
- Representing a chessboard using arrays
- Creating Python functions
- Using recursion
- Understanding backtracking
- Checking rows, columns, and diagonals
- Handling user input
- Handling invalid input using exceptions
- Solving a constraint-based problem
- Building a command-line application

## Project Structure

```text
N-Queens-Problem/
│
├── n queees.py
└── README.md
```

## Limitations

This project is a command-line implementation of the N-Queens problem.
The program displays the first valid solution it finds rather than displaying every possible solution.

## Internship

This project was completed as part of my Python Development Internship at Codveda Technologies.