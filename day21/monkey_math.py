from sys import argv

known = set()
unknown = set()
rules = dict()

with open(argv[1]) as f:
    for line in f:
        toks = line.rstrip().split(' ')
        monkey = toks[0][:4]
        if len(toks) == 2:
            rules[monkey] = int(toks[1])
            known.add(monkey)
        else:
            if toks[2] == '/':
                toks[2] = '//'
            rules[monkey] = toks[1], toks[2], toks[3]
            unknown.add(monkey)

while 'root' not in known:
    # evaluate everything we can
    removed = set()
    for monkey in unknown:
        rule = rules[monkey]
        if rule[0] in known and rule[2] in known:
            tok1 = rules[rule[0]]
            tok2 = rules[rule[2]]
            print(tok1, rule[1], tok2)
            rules[monkey] = eval(f'{tok1} {rule[1]} {tok2}')
            removed.add(monkey)
            known.add(monkey)
    if len(removed) == 0:
        print('nothing to remove')
        break
    else:
        print('removing', removed)
        unknown -= removed

print('Part 1:', rules['root'])
