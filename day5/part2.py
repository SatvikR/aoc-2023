def parse(data, strip=True):
    with open('input.txt') as f:
        n = f.readline()
        while n != '':
            data.append(n.strip() if strip else n)
            n = f.readline()

class Range:
    def __init__(self, start, length):
        self.start = start
        self.length = length
        self.end = start + length - 1

    def from_end(start, end):
        return Range(start, end - start + 1)

    def __str__(self):
        return f"{self.start} -> {self.end}"

class Mapping:
    def __init__(self):
        self.map = [] # each map will be [source, dest, length]

    def add_map(self, source, dest, length):
        for i, m in enumerate(self.map):
            s, d, l = m
            if source < s:
                self.map.insert(i, [source, dest, length])
                return
        self.map.append([source, dest, length])

    def find_map(self, range):
        for i, m in enumerate(self.map):
            s, _, l = m
            if s <= range.start < s + l:
                return i
        return -1

    def convert_ranges(self, ranges):
        converts = []
        for i, r in enumerate(ranges):
            # look for splits
            for m in self.map:
                s, _, _ = m
                if r.start < s <= r.end:
                    # split found!
                    # ranges[i] = Range(r.start, s - r.start)
                    # ranges.insert(i+1, Range(s, r.end - s + 1))
                    ranges[i] = Range.from_end(r.start, s-1)
                    ranges.insert(i+1, Range.from_end(s, r.end))
                    break

            # now we know that r[i] can be cleanly converted
            mapping = self.find_map(r)
            if mapping == -1:
                converts.append(r)
            else:
                start, dest, _ = self.map[mapping]
                converts.append(Range(r.start + dest - start, r.length))
            if converts[-1].start == 0:
                pass
                # print(r) print(converts[-1])

        return converts

def main():
    data = []
    parse(data)

    # parse seed ranges
    seeds = []
    raw_seeds = [int(x) for x in data[0].split()[1:]]
    for i in range(len(raw_seeds) // 2):
        seeds.append(Range(raw_seeds[2*i], raw_seeds[2*i+1]))

    seeds = [seeds[3]]

    # parse mappings
    data = data[2:]
    while len(data) > 0:
        m = Mapping()
        data = data[1:]
        while len(data[0]) > 0:
            dest, source, length = [int(x) for x in data[0].split()]
            m.add_map(source, dest, length)
            data = data[1:]
        # convert ranges over
        seeds = m.convert_ranges(seeds)
        print([str(x) for x in seeds])
        m = min(seeds, key=lambda x: x.start)
        data = data[1:]

    m = min(seeds, key=lambda x: x.start)
    print(m.start, m.end)


if __name__ == '__main__':
    main()
