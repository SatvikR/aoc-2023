def parse(data, dataset, strip=True):
    with open(dataset) as f:
        n = f.readline()
        while n != '':
            data.append(n.strip() if strip else n)
            n = f.readline()

def try_element(nav, directions, element):
    steps = 0
    curr = element

    while True:
        for c in directions:
            if curr == 'ZZZ':
                return steps
            if c == 'L':
                curr = nav[curr][0]
            else:
                curr = nav[curr][1]
            steps += 1

def solve(dataset):
    data = []
    parse(data, dataset)

    nav = {}

    directions = data[0]
    data[2:]

    for d in data:
        element = d[:3]
        left = d[7:10]
        right = d[12:15]
        nav[element] = [left, right]

    print(try_element(nav, directions, 'AAA'))

if __name__ == '__main__':
    print('--test--')
    solve('test.txt')
    print('--input--')
    solve('input.txt')