ids = []

with open('input.txt', 'r') as f:
    ids = f.readline().split(',')

total = 0

for i in ids:
    r = i.split('-')
    for j in range(int(r[0]), int(r[1])+1):
        s = str(j)
        if len(s) % 2 == 0:
            half = int(len(s)/2)
            if s[0:half] == s[half:]:
                total += int(j)

print(total)