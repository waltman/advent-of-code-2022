from sys import argv
from collections import deque
import re

class Monkey:
    def __init__(self, items, op_str, div_by, throw_true, throw_false):
        self.queue = deque(items)
        self.op = self._make_op(op_str)
        self.test = lambda x: throw_true if x % div_by == 0 else throw_false
        self.inspections = 0

    def _make_op(self, op_str):
        toks = op_str.split(' ')
        if toks[0] == '+':
            op_fn = lambda x: x + int(toks[1])
        elif toks[0] == '*':
            if toks[1] == 'old':
                op_fn = lambda x: x * x
            else:
                op_fn = lambda x: x * int(toks[1])
        return op_fn

    def empty(self):
        return len(self.queue) == 0

    def inspect(self):
        self.inspections += 1
        worry = self.queue.popleft()
        worry = self.op(worry)
        worry //= 3
        throw_to = self.test(worry)
        return worry, throw_to

    def append(self, worry):
        self.queue.append(worry)

# parse the input
monkeys = []
with open(argv[1]) as f:
    for line in f:
        line = line.rstrip()
        if m := re.search('Starting items: (.*)', line):
            items = [int(x) for x in m.group(1).split(', ')]
        elif m := re.search('Operation: new = old (.*)', line):
            op = m.group(1)
        elif m := re.search('Test: divisible by (\d+)', line):
            div_by = int(m.group(1))
        elif m := re.search('If true: throw to monkey (\d+)', line):
            throw_true = int(m.group(1))
        elif m := re.search('If false: throw to monkey (\d+)', line):
            throw_false = int(m.group(1))
            throw_fn = lambda x: throw_true if x % div_by else throw_false
            monkeys.append(Monkey(items, op, div_by, throw_true, throw_false))

for i in range(len(monkeys)):
    print(i, monkeys[i].queue)

for round in range(1, 21):
    for monkey in monkeys:
        while not monkey.empty():
            worry, throw_to = monkey.inspect()
            monkeys[throw_to].append(worry)

for i in range(len(monkeys)):
    print(i, monkeys[i].queue)

inspections = sorted([monkey.inspections for monkey in monkeys])
print('Part 1:', inspections[-1] * inspections[-2])

