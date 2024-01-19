data = []

with open('input.txt') as f:
    n = f.readline()
    while n != '':
        data.append(n.strip())
        n = f.readline()

def check_cell(r, c):
    if r < 0 or r >= len(data) or c < 0 or c >= len(data[0]):
        return False
    return not data[r][c].isdigit() and not data[r][c] == '.'

def check_surrounding(r, c0, cf):
    for i in range(c0-1, cf+2):
        if check_cell(r-1, i) or check_cell(r+1, i):
            return True
    return check_cell(r, c0-1) or check_cell(r, cf+1)

def main():
    total = 0
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
                if check_surrounding(r, c0, cf):
                    total += int(num)
            else:
                c += 1
    print(total)




if __name__ == '__main__':
    main()