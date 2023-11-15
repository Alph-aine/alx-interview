#!/usr/bin/python3
'''Places N queens on a chessboard without posing any threat to each other'''

import sys


def is_safe(board, row, col, n):
    '''Check if there is a queen in the same row'''
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check if there is a queen in the upper diagonal on the left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check if there is a queen in the lower diagonal on the left side
    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def print_solution(board, n):
    '''prints solution'''
    solution = []
    for i in range(n):
        row = []
        for j in range(n):
            if board[i][j] == 1:
                row.append([i, j])
        solution.append(row)

    print(solution)


def solve_nqueens_util(board, col, n):
    '''recursively prints solution for n sized board'''
    if col == n:
        print_solution(board, n)
        return

    for i in range(n):
        if is_safe(board, i, col, n):
            board[i][col] = 1
            solve_nqueens_util(board, col + 1, n)
            board[i][col] = 0


def solve_nqueens(n):
    '''Main function'''
    if not isinstance(n, int):
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [[0] * n for _ in range(n)]
    solve_nqueens_util(board, 0, n)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    solve_nqueens(N)
