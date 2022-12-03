from sys import argv

def priority(ch):
    if 'a' <= ch <= 'z':
        return ord(ch) - ord('a') + 1
    else:
        return ord(ch) - ord('A') + 27

def common_item(c1, c2):
    return list({c for c in c1} & {c for c in c2})[0]

def group_badge(rucks):
    common = {c for c in rucks[0]}
    for i in range(1,len(rucks)):
        common &= {c for c in rucks[i]}
    return list(common)[0]

score = 0
group_score = 0
with open(argv[1]) as f:
    rucks = []
    for line in f:
        line = line.rstrip()
        middle = len(line) // 2
        common = common_item(line[:middle], line[middle:])
        score += priority(common)
        rucks.append(line)
        if len(rucks) == 3:
            badge = group_badge(rucks)
            group_score += priority(badge)
            rucks = []

print('Part 1:', score)
print('Part 2:', group_score)

    
