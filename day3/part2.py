data = []

with open('input.txt') as f:
    n = f.readline()
    while n != '':
        data.append(n.strip())
        n = f.readline()

def key(r, c):
    return 2**r * 3**c

def check_cell(r, c, num, gears):
    if r < 0 or r >= len(data) or c < 0 or c >= len(data[0]):
        return False
    if not data[r][c].isdigit() and not data[r][c] == '.':
        if data[r][c] == '*':
            if key(r, c) in gears:
                gears[key(r, c)].append(num)
            else:
                gears[key(r, c)] = [num]
        return True
    return False

def check_surrounding(r, c0, cf, num, gears):
    # we check all, even if redundant, to find gears
    t = False
    for i in range(c0-1, cf+2):
        if check_cell(r-1, i, num, gears) or check_cell(r+1, i, num, gears):
            t = True
    if check_cell(r, c0-1, num, gears) or check_cell(r, cf+1, num, gears):
        True
    return t

def main():
    gears = {}
    for r, d in enumerate(data):
        c = 0
        while c < len(data):
            if d[c].isdigit():
                c0 = c
                cf = c
                num = d[c]
                for j in range(c+1, len(d)):
                    if not d[j].isdigit():
                        break
                    num += d[j]
                    cf = j
                c += len(num)
                check_surrounding(r, c0, cf, int(num), gears)
            else:
                c += 1
    total = 0
    for i in gears:
        if len(gears[i]) == 2:
            total += gears[i][0] * gears[i][1]
    print(total)




if __name__ == '__main__':
    main()