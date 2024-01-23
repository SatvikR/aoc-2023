data = []

with open('input.txt') as f:
    n = f.readline()
    while n != '':
        data.append(n)
        n = f.readline()



total = 0

for d in data:
    first = 0
    last = 0
    for c in d:
        if ord('1') <= ord(c) <= ord('9'):
            if first == 0:
                first = int(c)
                last = first
            else:
                last = int(c)
    total += first * 10 + last

print(total)