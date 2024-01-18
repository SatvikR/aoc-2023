data = []

with open('input.txt') as f:
    n = f.readline()
    while n != '':
        data.append(n)
        n = f.readline()

total = 0

for d in data:
    d = d[5::]
    id = d[:d.index(':'):]
    d = d[2+len(id)::]
    pulls = d.split(';')

    amts = {
        'red': 0,
        'green': 0,
        'blue': 0
    }
    for p in pulls:
        rocks = p.split(',')
        for r in rocks:
            amt, clr = r.strip().split(' ')
            if int(amt) > amts[clr]:
                amts[clr] = int(amt)
    i = 1
    for j in amts.values():
        i *= j
    total += i

print(total)
