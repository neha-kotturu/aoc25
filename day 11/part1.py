from collections import defaultdict

with open('input.txt', 'r') as f:
    lines = f.readlines()
    devices = [line.strip().split() for line in lines]

graph = defaultdict(list)

for parts in devices:
    device = parts[0].rstrip(":")
    outputs = parts[1:]
    graph[device].extend(outputs)

def count_paths(curr, end):
    if curr == end:
        return 1

    total = 0

    for next in graph[curr]:
        total += count_paths(next, end)

    return total


print(count_paths("you", "out"))