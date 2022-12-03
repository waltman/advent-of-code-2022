from sys import argv

def priority(ch):
    if 'a' <= ch <= 'z':
        return ord(ch) - ord('a') + 1
    else:
        return ord(ch) - ord('A') + 27

def common_item(c1, c2):
    return list({c for c in c1} & {c for c in c2})[0]

score = 0
with open(argv[1]) as f:
    for line in f:
        line = line.rstrip()
        middle = len(line) // 2
        common = common_item(line[:middle], line[middle:])
        score += priority(common)

print('Part 1:', score)

    
