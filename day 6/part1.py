rows = []

with open('input.txt', 'r') as f:

    lines = f.readlines()
    lines = [line.strip().split() for line in lines]
    rows = [list(row) for row in list(zip(*lines))]



total = 0

for row in rows:
    operation = row[-1]
    curr = 0 if operation == '+' else 1
    for i in row[:-1]:
        curr = curr+int(i) if operation == '+' else curr*int(i)
    total += curr

print(total)