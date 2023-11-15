#!/usr/bin/python3
'''Places N queens on a chessboard without posing any threat to each other'''

import sys


def is_safe(board, row, col, n):
    """
    Check if it's safe to place a queen at the given position on the board.

    Args:
        board (list): The current state of the chessboard.
        row (int): The row to check.
        col (int): The column to check.
        n (int): The size of the board.

    Returns:
        bool: True if it's safe, False otherwise.
    """
    # Check if there is a queen in the same row
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on the left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on the left side
    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solve_nqueens_util(board, col, n, result):
    """
    Recursive utility function to solve the N-Queens problem.

    Args:
        board (list): The current state of the chessboard.
        col (int): The current column to consider.
        n (int): The size of the board.
        result (list): List to store the solutions.

    Returns:
        None
    """
    if col == n:
        solution = []
        for i in range(n):
            for j in range(n):
                if board[i][j] == 1:
                    solution.append([i, j])
        result.append(solution)
        return

    for i in range(n):
        if is_safe(board, i, col, n):
            board[i][col] = 1
            solve_nqueens_util(board, col + 1, n, result)
            board[i][col] = 0


def solve_nqueens(n):
    """
    Solve the N-Queens problem for a given board size.

    Args:
        n (int): The size of the board.

    Returns:
        list: List of solutions,
        where each solution is a list of queen positions.
    """
    result = []
    board = [[0 for _ in range(n)] for _ in range(n)]
    solve_nqueens_util(board, 0, n, result)
    return result


def print_solutions(solutions):
    """
    Print the solutions for the N-Queens problem.

    Args:
        solutions (list): List of solutions,
        where each solution is a list of queen positions.

    Returns:
        None
    """
    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
        if n < 4:
            raise ValueError("N must be at least 4")
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    solutions = solve_nqueens(n)
    print_solutions(solutions)
