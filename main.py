def is_valid(board, row, col):
    # Check if the row on left side is safe
    for i in range(col):
        if board[i] == row or \
           abs(board[i] - row) == abs(i - col):
            return False
    return True

def solve_n_queens_util(board, col, n):
    # If all queens are placed, then return True
    if col >= n:
        return True

    # Consider this column and try placing this queen in all rows one by one
    for i in range(n):
        if is_valid(board, i, col):
            # Place this queen in board[i][col]
            board[col] = i

            # Recur to place rest of the queens
            if solve_n_queens_util(board, col + 1, n):
                return True

            # If placing queen in board[i][col] doesn't lead to a solution, then
            # remove queen from board[i][col] (Backtrack)
            board[col] = -1

    # If the queen cannot be placed in any row in this column, then return False
    return False

def solve_n_queens(n):
    board = [-1] * n  # Initialize the board
    if not solve_n_queens_util(board, 0, n):
        print("Solution does not exist")
        return []
    else:
        # Print and return the solution
        return [[('Q' if board[j] == i else '.') for j in range(n)] for i in range(n)]

# Test the function with N=4
n = 5
solution = solve_n_queens(n)
for row in solution:
    print(' '.join(row))
