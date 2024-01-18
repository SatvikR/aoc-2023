data = []

with open('test.txt') as f:
    n = f.readline()
    while n != '':
        data.append(n)
        n = f.readline()

total = 0

numbers = [
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine"
]

total = 0

for d in data:
    first = 0
    last = 0
    for i, c in enumerate(d):
        if ord('1') <= ord(c) <= ord('9'):
            if first == 0:
                first = int(c)
                last = first
            else:
                last = int(c)
        else:
            buf = d[i:i+5:]
            for j, n in enumerate(numbers):
                if buf.startswith(n):
                    if first == 0:
                        first = j+1
                        last = first
                    else:
                        last = j+1

    print(f"{first}{last}  {d}")
    total += first * 10 + last

print(total)
