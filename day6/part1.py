from math import sqrt, floor, ceil

def parse(data, dataset, strip=True):
    with open(dataset) as f:
        n = f.readline()
        while n != '':
            data.append(n.strip() if strip else n)
            n = f.readline()

def solve(dataset):
    data = []
    parse(data, dataset)

    times = [int(x) for x in data[0].split()[1:]]
    distances = [int(x) for x in data[1].split()[1:]]
    winners = 1

    for i in range(len(times)):
        t = times[i]
        d = distances[i]
        # using quadratic formula
        r1 = (t - sqrt(t ** 2 - 4 * d)) / 2
        r2 = (t + sqrt(t ** 2 - 4 * d)) / 2
        r1 = ceil(r1) if r1 // 1 != r1 else r1 + 1
        r2 = floor(r2) if r2 // 1 != r2 else r2 - 1
        winners *= r2 - r1 + 1


    print(winners)




if __name__ == '__main__':
    print('--test--')
    solve('test.txt')
    print('--input--')
    solve('input.txt')