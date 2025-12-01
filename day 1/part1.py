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
        curr = (curr - val) % 100
    else:
        curr = (curr + val) % 100

    if curr == 0:
        count += 1

print(count)