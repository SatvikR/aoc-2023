data = []

def parse(strip=True):
    with open('input.txt') as f:
        n = f.readline()
        while n != '':
            data.append(n.strip() if strip else n)
            n = f.readline()

def main():
    parse()
    total = 0

    for d in data:
        d = d[d.index(':')+1::]
        winners = set({})
        while d[1] != '|':
            winners.add(int(d[:3:].strip()))
            d = d[3::]

        d = d[2::]
        winning = 0
        while len(d) > 0:
            n = int(d[:3:].strip())
            if n in winners:
                winning += 1
            d = d[3::]

        if winning:
            total += 2 ** (winning-1)

    print(total)

if __name__ == '__main__':
    main()