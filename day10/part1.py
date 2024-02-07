from sys import setrecursionlimit
from math import ceil

def parse(data, dataset, strip=True):
    with open(dataset) as f:
        n = f.readline()
        while n != '':
            data.append(n.strip() if strip else n)
            n = f.readline()

class Node:
    def __init__(self, row, col, val):
        self.row = row
        self.col = col
        self.val = val
        self.distance = 0

    def get_openings(self):
        match self.val:
            case '|':
                return (self.row-1, self.col), (self.row+1, self.col)
            case '-':
                return (self.row, self.col-1), (self.row, self.col+1)
            case 'L':
                return (self.row-1, self.col), (self.row, self.col+1)
            case 'J':
                return (self.row-1, self.col), (self.row, self.col-1)
            case '7':
                return (self.row+1, self.col), (self.row, self.col-1)
            case 'F':
                return (self.row+1, self.col), (self.row, self.col+1)
        return (-1, -1), (-1, -1)


# given that r1, c1 exists
def equivalent(nodes, r1, c1, r2, c2):
    if valid(r2, c2, nodes):
        return (r1, c1) == (r2, c2)
    return False


def valid(row, col, nodes):
    return 0 <= row < len(nodes) and 0 <= col < len(nodes[0])


def dfs(prev, curr, distance, nodes):
    if curr.val == 'S':
        return None

    (r1, c1), (r2, c2) = curr.get_openings()
    r, c = 0, 0
    if equivalent(nodes, prev.row, prev.col, r1, c1):
        r, c = r2, c2
    else:
        r, c, = r1, c1

    curr.distance = distance
    if valid(r, c, nodes):
        return curr, nodes[r][c], distance + 1, nodes
    return None


def solve(dataset):
    data = []
    parse(data, dataset)

    nodes = []
    starting = Node(0, 0, 0)
    for i, row in enumerate(data):
        curr = []
        for j, e in enumerate(row):
            curr.append(Node(i, j, e))
            if curr[-1].val == 'S':
                starting = curr[-1]
        nodes.append(curr)

    for dr, dc in [
        (-1, 0),
        (1, 0),
        (0, 1),
        (0, -1),
    ]:
        if valid(starting.row + dr, starting.col + dc, nodes):
            next = nodes[starting.row + dr][starting.col + dc]
            if (starting.row, starting.col) in list(next.get_openings()):
                # loop is here to get around pythons recursive limit
                # and to save memory
                d = starting, next, 1, nodes
                while True:
                    prev, curr, distance, nodes = d
                    d = dfs(prev, curr, distance, nodes)
                    if d == None:
                        break
    m = -1
    for row in nodes:
        for e in row:
            if e.distance > m:
                m = e.distance
    print(ceil(m/2))


if __name__ == '__main__':
    print('--test--')
    solve('test.txt')
    print('--input--')
    solve('input.txt')