rows = []

with open('input.txt', 'r') as f:

    lines = f.readlines()
    for line in lines:
        rows.append(line.strip())


directions = [(-1,-1),(0,-1),(1,-1),(-1,0),(1,0),(-1,1),(0,1),(1,1)]

total = 0

for i in range(len(rows)):
    r = rows[i]
    for j in range(len(r)):
        if r[j] == '@':
            cnt = 0
            for d in directions:
                    x = j+d[0] if j+d[0] >= 0 and j+d[0] < len(r) else -1
                    y = i+d[1] if i+d[1] >= 0 and i+d[1] < len(rows) else -1
                    if x>=0 and y>=0:
                        if rows[y][x] == '@':
                            cnt += 1
            if cnt < 4:
                 total += 1

print(total)