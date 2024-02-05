def parse(data, dataset, strip=True):
    with open(dataset) as f:
        n = f.readline()
        while n != '':
            data.append(n.strip() if strip else n)
            n = f.readline()

def find_next(row):
    sub_rows = []
    curr = row

    all_zero = False
    while not all_zero:
        all_zero = True
        diff = []
        for i in range(0, len(curr) - 1):
            d = curr[i+1] - curr[i]
            diff.append(d)
            all_zero = all_zero and d == 0
        sub_rows.append(diff)
        curr = diff

    sub_rows = sub_rows[::-1]
    sub_rows.append(row)
    for i in range(1, len(sub_rows)):
        sub_rows[i].append(sub_rows[i][-1] + sub_rows[i-1][-1])
    return sub_rows[-1][-1]


def solve(dataset):
    data = []
    parse(data, dataset)

    total = 0
    for d in data:
        total += find_next([int(x) for x in d.split()])
    print(total)


if __name__ == '__main__':
    print('--test--')
    solve('test.txt')
    print('--input--')
    solve('input.txt')