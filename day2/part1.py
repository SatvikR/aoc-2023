data = []

with open('input.txt') as f:
    n = f.readline()
    while n != '':
        data.append(n)
        n = f.readline()

total = 0
amts = {
    'red': 12,
    'green': 13,
    'blue': 14
}

for d in data:
    d = d[5::]
    id = d[:d.index(':'):]
    d = d[2+len(id)::]
    pulls = d.split(';')
    valid = True

    for p in pulls:
        rocks = p.split(',')
        for r in rocks:
            amt, clr = r.strip().split(' ')
            if int(amt) > amts[clr]:
                valid = False
                break
        if not valid:
            break

    if valid:
        total += int(id)

print(total)
