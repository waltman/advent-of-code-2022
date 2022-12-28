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

with open(argv[1]) as f:
    for line in f:
        line = line.strip()
        print(line, snafu2dec(line))
