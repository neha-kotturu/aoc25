banks = []

with open('input.txt', 'r') as f:

    lines = f.readlines()
    for line in lines:
        banks.append(line.strip())


total = 0

for bank in banks:
    battery = ''
    val = battery
    idx = 0

    for i in range(11, -1, -1):
        remaining = bank[idx:-i] if i != 0 else bank[idx:]
        next_val = max(remaining)
        battery += next_val
        val = next_val
        idx = bank.index(val, idx) + 1
    
    total += int(battery)

print(total)

    