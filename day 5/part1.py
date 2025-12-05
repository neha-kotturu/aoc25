rows = []

with open('input.txt', 'r') as f:

    lines = f.readlines()
    for line in lines:
        rows.append(line.strip())

idx = rows.index('')
ranges = rows[0:idx]
ingredients = rows[idx+1:]


total = 0

for i in ingredients:
    for j in ranges:
        range = j.split('-')
        if int(i) >= int(range[0]) and int(i) <= int(range[1]):
            total += 1
            break

print(total)