from functools import cache

board = []

with open('input.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
        board.append(list(line.strip()))

start = [(r,c) for r, row in enumerate(board) for c, char in enumerate(row) if char == 'S'][0]

@cache
def path(r,c):
    if r >= len(board): 
        return 1
    if board[r][c] == '.' or board[r][c] == 'S':
        return path(r+1, c)
    elif board[r][c] == "^":
        return path(r, c-1) + path(r, c+1)
    
print(path(start[0], start[1]))