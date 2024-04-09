#!/usr/bin/python3
"""
Solution to the nqueens problem
"""
import sys


def backtrack(row, n, cols, pos_diagonal, neg_diagonal, board):
    """
    Backtrack function to find solutions to the N-queens problem
    """
    if row == n:
        res = []
        for r in range(len(board)):
            for c in range(len(board[r])):
                if board[r][c] == 1:
                    res.append([r, c])
        print(res)
        return

    for col in range(n):
        if col in cols or (row + col) in pos_diagonal or (row - col) in neg_diagonal:
            continue

        cols.add(col)
        pos_diagonal.add(row + col)
        neg_diagonal.add(row - col)
        board[row][col] = 1

        backtrack(row + 1, n, cols, pos_diagonal, neg_diagonal, board)

        cols.remove(col)
        pos_diagonal.remove(row + col)
        neg_diagonal.remove(row - col)
        board[row][col] = 0


def nqueens(n):
    """
    Solves the N-queens problem for a given board size n
    Args:
        n (int): Size of the chessboard and number of queens
    """
    cols = set()
    pos_diagonal = set()
    neg_diagonal = set()
    board = [[0] * n for _ in range(n)]

    backtrack(0, n, cols, pos_diagonal, neg_diagonal, board)


if __name__ == "__main__":
    args = sys.argv
    if len(args) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        n_value = int(args[1])
        if n_value < 4:
            print("N must be at least 4")
            sys.exit(1)
        nqueens(n_value)
    except ValueError:
        print("N must be a number")
        sys.exit(1)
