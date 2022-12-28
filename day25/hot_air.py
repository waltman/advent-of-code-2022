from sys import argv

def snafu2dec(line):
    res = 0
    pwr = 1
    for i in range(len(line)-1,-1,-1):
        match line[i]:
            case '2':
                res += 2 * pwr
            case '1':
                res += pwr
            case '-':
                res += -pwr
            case '=':
                res += -2 * pwr
        pwr *= 5
    return res

def dec2snafu(val):
    res = ''

    while val:
        digit = val % 5
        rest = val // 5
        if 0 <= digit <= 2:
            res = str(digit) + res
        elif digit == 3:
            res = '=' + res
            rest += 1
        else:
            res = '-' + res
            rest += 1
        val = rest
    return res

tot = 0
with open(argv[1]) as f:
    for line in f:
        line = line.strip()
        print(line, snafu2dec(line), dec2snafu(snafu2dec(line)))
        tot += snafu2dec(line)

print('Part 1:', dec2snafu(tot))
