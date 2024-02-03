from math import lcm

def parse(data, dataset, strip=True):
    with open(dataset) as f:
        n = f.readline()
        while n != '':
            data.append(n.strip() if strip else n)
            n = f.readline()

def solve(dataset):
    data = []
    parse(data, dataset)

    nav = {}

    directions = data[0]
    data = data[2:]

    for d in data:
        element = d[:3]
        left = d[7:10]
        right = d[12:15]
        nav[element] = [left, right]

    ghosts = [e for e in nav if e[2] == 'A']
    coefs = []
    for g in ghosts:
        curr = g
        steps = 0
        done = False
        while not done:
            for d in directions:
                next = 0 if d == 'L' else 1
                curr = nav[curr][next]
                steps += 1
                done = curr[2] == 'Z'
                if done:
                    break
        coefs.append(steps)

    print(lcm(*coefs))

if __name__ == '__main__':
    print('--test--')
    solve('test.txt')
    print('--input--')
    solve('input.txt')