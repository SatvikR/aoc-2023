def parse(data, dataset, strip=True):
    with open(dataset) as f:
        n = f.readline()
        while n != '':
            data.append(n.strip() if strip else n)
            n = f.readline()

def solve(dataset):
    data = []
    parse(data, dataset)

    img = []
    nodes = []

    e_rows = 0
    e_cols = 0
    for i, row in enumerate(data):
        empty = True
        curr = []
        for e in row:
            empty = empty and e == '.'
            curr.append([e, i + e_rows, 0])
        img.append(curr)
        if empty:
            e_rows += 1

    for j in range(len(data[0])):
        empty = True
        for i, row in enumerate(data):
            empty = empty and row[j] == '.'
            img[i][j][2] = j + e_cols
            if img[i][j][0] == '#':
                nodes.append(img[i][j])
        if empty:
            e_cols += 1


    total = 0
    for i in range(len(nodes)):
        for j in range(i+1, len(nodes)):
            _, x0, y0 = nodes[i]
            _, x1, y1 = nodes[j]
            total += abs(x1 - x0) + abs(y1 - y0)
    print(total)


if __name__ == '__main__':
    print('--test--')
    solve('test.txt')
    print('--input--')
    solve('input.txt')