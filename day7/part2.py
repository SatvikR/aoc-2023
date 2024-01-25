from functools import cmp_to_key

def parse(data, dataset, strip=True):
    with open(dataset) as f:
        n = f.readline()
        while n != '':
            data.append(n.strip() if strip else n)
            n = f.readline()

def calculate_type(hand):
    freq = {}
    for i in hand:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1

    if len(freq) == 1: # five of a kind (done before J conversion bc JJJJJ is good)
        return 6

    # here exists the joker problem
    if 'J' in freq:
        js = freq['J']
        del freq['J']
        k = ''
        m = 0
        for f in freq:
            if freq[f] > m:
                m = freq[f]
                k = f
        freq[k] += js

    if len(freq) == 1: # five of a kind (we have to check again bc of jokers)
        return 6
    if len(freq) == 2:
        if max(freq.values()) == 4: # four of a kind
            return 5
        return 4 # full house
    if len(freq) == 3:
        if max(freq.values()) == 3:
            return 3 # three of a kind
        return 2 # two pair
    if len(freq) == 4:
        return 1 # one pair
    return 0 # high card

# -1 if h0 < h1, 1 if h0 > h1
def compare_similar_hands(hand0, hand1):
    h0, _ = hand0
    h1, _ = hand1
    order = ['A', 'K', 'Q', 'T']

    for i in range(5):
        if h0[i] == h1[i]:
            continue
        if h0[i] in order:
            if h1[i] not in order:
                return True
            return order.index(h0[i]) < order.index(h1[i])
        if h1[i] in order:
            return False
        if h0[i] == 'J':
            return False
        if h1[i] == 'J':
            return True
        return int(h0[i]) > int(h1[i])

def solve(dataset):
    data = []
    parse(data, dataset)

    hands = {
        0: [],
        1: [],
        2: [],
        3: [],
        4: [],
        5: [],
        6: []
    }

    for d in data:
        hand, bid = d.split()
        hands[calculate_type(hand)].append((hand, int(bid)))

    for i in range(7):
        hands[i] = sorted(hands[i],
            key=cmp_to_key(
                lambda h0, h1: 1 if compare_similar_hands(h0, h1) else -1)
        )

    total = 0
    rank = 1
    for i in range(7):
        for hand in hands[i]:
            _, bid = hand
            total += bid * rank
            rank += 1

    print(total)

if __name__ == '__main__':
    print('--test--')
    solve('test.txt')
    print('--input--')
    solve('input.txt')