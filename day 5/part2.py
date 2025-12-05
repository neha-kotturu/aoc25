rows = []

with open('input.txt', 'r') as f:

    lines = f.readlines()
    for line in lines:
        rows.append(line.strip())

idx = rows.index('')
ranges = rows[0:idx]

intervals = []

for r in ranges:
    a, b = map(int, r.split('-'))
    intervals.append((a, b))

intervals.sort()

merged = []
curr_start, curr_end = intervals[0]

for start, end in intervals[1:]:
    if start <= curr_end + 1:
        curr_end = max(curr_end, end)
    else:
        merged.append((curr_start, curr_end))
        curr_start, curr_end = start, end

merged.append((curr_start, curr_end))

total = sum(end - start + 1 for start, end in merged)
print(total)
