from collections import deque

board = []

with open('input.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
        board.append(list(line.strip()))

start = [(r,c) for r, row in enumerate(board) for c, char in enumerate(row) if char == 'S'][0]
beams = deque([start])
seen = {start}

def add(r, c):
    if (r,c) in seen: 
        return
    seen.add((r,c))
    beams.append((r,c))

count = 0

#bfs
while len(beams) > 0:
    r, c = beams.popleft()
    if board[r][c] == "." or board[r][c] == "S":
        if r == len(board)-1: 
            continue
        add(r+1, c)
    elif board[r][c] == "^":
        add(r, c+1)
        add(r, c-1)
        count += 1

print(count)