def print_board(board):
    print("\n---------- CHESSBOARD ----------")

    for row in board:
        print(" ".join(row))

    print("________________________________")


def is_safe(board, row, col, n):

    # Check the same column
    for i in range(row):
        if board[i][col] == "Q":
            return False

    # Check upper-left diagonal
    i = row - 1
    j = col - 1

    while i >= 0 and j >= 0:
        if board[i][j] == "Q":
            return False

        i -= 1
        j -= 1

    # Check upper-right diagonal
    i = row - 1
    j = col + 1

    while i >= 0 and j < n:
        if board[i][j] == "Q":
            return False

        i -= 1
        j += 1

    return True


def solve_n_queens(board, row, n):

    # All queens have been successfully placed
    if row == n:
        return True

    # Try every column in the current row
    for col in range(n):

        if is_safe(board, row, col, n):

            # Place the queen
            board[row][col] = "Q"

            # Move to the next row
            if solve_n_queens(board, row + 1, n):
                return True

            # Backtrack
            board[row][col] = "."

    return False


def main():

    print("---------- N-QUEENS SOLVER ----------")
    

    try:
        n = int(input("Enter the number of queens: "))

        if n < 1:
            print("Please enter a number greater than 0.")
            return

        board = [["." for _ in range(n)] for _ in range(n)]

        if solve_n_queens(board, 0, n):
            print("\nSolution found!")
            print_board(board)

        else:
            print("\nNo solution exists for", n, "queens.")

    except ValueError:
        print("Invalid input. Please enter a whole number.")


if __name__ == "__main__":
    main()
