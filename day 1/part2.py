rotations = []

with open('input.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
        rotations.append(line.strip())

count = 0
curr = 50

for r in rotations:
    dir = r[0]
    val = int(r[1:])
    
    if dir == 'L':
        for step in range(1, val + 1):
            new_pos = (curr - step) % 100
            if new_pos == 0:
                count += 1
        curr = (curr - val) % 100
    else:
        for step in range(1, val + 1):
            new_pos = (curr + step) % 100
            if new_pos == 0:
                count += 1
        curr = (curr + val) % 100

print(count)