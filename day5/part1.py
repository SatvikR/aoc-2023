def parse(data, strip=True):
    with open('input.txt') as f:
        n = f.readline()
        while n != '':
            data.append(n.strip() if strip else n)
            n = f.readline()

class Map:
    def __init__(self):
        self.ranges = [] # each range will be [source, dest, length]

    def add_range(self, source, dest, length):
        i = len(self.ranges)
        for j, r in enumerate(self.ranges):
            if source < r[0]:
                i = j
                break

        self.ranges.insert(i, [source, dest, length])

    def convert_source(self, seed):
        if seed < self.ranges[0][0]:
            return seed

        i = len(self.ranges) - 1
        for j, r in enumerate(self.ranges):
            if seed < r[0]:
                i = j - 1
                break

        source, dest, length = self.ranges[i]
        if seed < source + length:
            return dest + seed - source
        else:
            return seed

def main():
    data = []
    parse(data)

    seeds = [int(x) for x in data[0].split()[1::]]
    data = data[1::]

    while len(data) > 0:
        data = data[2::]
        m = Map()
        while len(data) > 0:
            if data[0] == '':
                break

            dest, source, length = [int(x) for x in data[0].split()]
            m.add_range(source, dest, length)
            data = data[1::]

        for i in range(len(seeds)):
            seeds[i] = m.convert_source(seeds[i])

    print(min(seeds))


if __name__ == '__main__':
    main()