from sys import argv

round_score = {
    'AX': 3,
    'AY': 6,
    'AZ': 0,
    'BX': 0,
    'BY': 3,
    'BZ': 6,
    'CX': 6,
    'CY': 0,
    'CZ': 3,
}

my_score = {
    'X': 1,
    'Y': 2,
    'Z': 3,
}

part2_pick = {
    'AX': 'Z', # 0 + 3
    'AY': 'X', # 3 + 1
    'AZ': 'Y', # 6 + 2
    'BX': 'X', # 0 + 1
    'BY': 'Y', # 3 + 2
    'BZ': 'Z', # 6 + 3
    'CX': 'Y', # 0 + 2
    'CY': 'Z', # 3 + 3
    'CZ': 'X', # 6 + 1
}

part2_score = {
    'AX': 0 + 3,
    'AY': 3 + 1,
    'AZ': 6 + 2,
    'BX': 0 + 1,
    'BY': 3 + 2,
    'BZ': 6 + 3,
    'CX': 0 + 2,
    'CY': 3 + 3,
    'CZ': 6 + 1,
}

total_score = 0
total_score2 = 0
with open(argv[1]) as f:
    for line in f:
        them, me = line.rstrip().split(' ')
        total_score += round_score[them+me] + my_score[me]
        total_score2 += part2_score[them+me]

print('Part 1:', total_score)
print('Part 2:', total_score2)
