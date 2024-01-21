data = []

def parse(strip=True):
    with open('input.txt') as f:
        n = f.readline()
        while n != '':
            data.append(n.strip() if strip else n)
            n = f.readline()

def calculate_winners(d):
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

    return winning

def main():
    parse()
    cards = [1] * len(data)

    for i, d in enumerate(data):
        w = calculate_winners(d)
        for j in range(i+1, i+w+1):
            cards[j] += cards[i]

    print(sum(cards))

if __name__ == '__main__':
    main()