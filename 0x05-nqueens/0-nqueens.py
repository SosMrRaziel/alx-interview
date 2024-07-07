#!/usr/bin/python3
""" N queens problem """
import sys


def print_solution(board):
    """ Print the solution"""
    solution = [[i, board[i]] for i in range(len(board))]
    print(solution)


def is_safe(board, row, col):
    """ Check if a queen can be placed on board[row][col]"""
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True


def solve_nqueens(board, row):
    """ Solve the N queens problem"""
    if row == len(board):
        print_solution(board)
        return
    for col in range(len(board)):
        if is_safe(board, row, col):
            board[row] = col
            solve_nqueens(board, row + 1)


def main():
    """ Main function"""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)
    board = [-1] * N
    solve_nqueens(board, 0)


if __name__ == "__main__":
    main()
