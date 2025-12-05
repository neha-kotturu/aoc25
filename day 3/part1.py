banks = []

with open('input.txt', 'r') as f:

    lines = f.readlines()
    for line in lines:
        banks.append(line.strip())


total = 0

for bank in banks:
    # b = list(bank[0:len(bank)-1])
    b = bank[0:len(bank)-1]
    first = max(b)
    second = max(bank[b.index(first)+1:])
    total += int(first + second)

print(total)
