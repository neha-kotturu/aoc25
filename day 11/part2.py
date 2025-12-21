from collections import defaultdict
from functools import cache

with open('input.txt', 'r') as f:
    lines = f.readlines()
    devices = [line.strip().split() for line in lines]

graph = defaultdict(list)

for parts in devices:
    device = parts[0].rstrip(":")
    outputs = parts[1:]
    graph[device] = outputs


@cache
def count_paths(curr, end, dac, fft):
    if curr == "dac":
        dac = True
    if curr == "fft":
        fft = True

    if curr == end:
        return 1 if dac and fft else 0

    total = 0
    for next in graph[curr]:
        total += count_paths(next, end, dac, fft)

    return total


print(count_paths("svr", "out", False, False))
