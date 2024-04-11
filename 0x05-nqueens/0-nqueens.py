#!/usr/bin/python3
'''
0x05. N Queens
'''
import sys


def is_safe(board, row, col, N):
    '''Check if there's a queen in the same column'''
    for i in range(row):
        if board[i][col] == 'Q':
            return False
    '''Check upper left diagonal'''
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 'Q':
            return False
    '''Check upper right diagonal'''
    for i, j in zip(range(row, -1, -1), range(col, N)):
        if board[i][j] == 'Q':
            return False
    return True


def solve(board, row, N):
    if row == N:
        for row in board:
            print(''.join(row))
        print()
        return
    for col in range(N):
        if is_safe(board, row, col, N):
            board[row][col] = 'Q'
            solve(board, row + 1, N)
            board[row][col] = '.'


def nqueens(N):
    if not N.isdigit():
        print("N must be a number")
        sys.exit(1)
    N = int(N)
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)
    board = [['.' for _ in range(N)] for _ in range(N)]
    solve(board, 0, N)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    nqueens(sys.argv[1])
