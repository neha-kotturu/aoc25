rows = []

with open('input.txt', 'r') as f:
    lines = f.readlines()
    lines = [line.strip('\n') for line in lines]
    rows = [list(row) for row in list(zip(*lines))]


operation = ''
total = 0
curr = 0 if rows[1][-1] == '+' else 1
change = False

for i in rows:
    operation = i[-1] if i[-1] != ' ' else operation    
    if change:
        curr = 0 if operation == '+' else 1
        change = False
    num = ''.join(i[:-1])
    if num.strip().isdigit():
        curr = curr+int(num) if operation == '+' else curr*int(num)
    else:
        total += curr
        change = True

total += curr

print(total)