from sys import argv
from copy import copy

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
#            if toks[2] == '/':
#                toks[2] = '//'
            rules[monkey] = toks[1], toks[2], toks[3]
            unknown.add(monkey)

rules_save = copy(rules)
unknown_save = copy(unknown)
known_save = copy(known)
low = 3327729446658
high = 3435075557698
done = False
while not done:
    rules = copy(rules_save)
    known = copy(known_save)
    unknown = copy(unknown_save)
    rules['humn'] = (high + low) // 2
    while 'root' not in known:
        # evaluate everything we can
        removed = set()
        for monkey in unknown:
            rule = rules[monkey]
            if rule[0] in known and rule[2] in known:
                tok1 = rules[rule[0]]
                tok2 = rules[rule[2]]
                if monkey == 'root':
                    delta = tok1 - tok2
                    print(rules['humn'], tok1, tok2, delta)
                    if delta == 0:
                        print('Part 2:', rules['humn'])
                        done = True
                    else:
                        if delta > 0:
                            low = rules['humn'] + 1
                        else:
                            high = rules['humn'] - 1
                    known.add('root')
 #                   break
                rules[monkey] = eval(f'{tok1} {rule[1]} {tok2}')
                removed.add(monkey)
                known.add(monkey)
        if len(removed) == 0:
            break
        else:
            unknown -= removed

#    print('Part 2:', rules['root'])
