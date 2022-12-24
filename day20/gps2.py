from sys import argv
from copy import copy

class Node:
    def __init__(self, val):
        self.val = val
        self.pred = self.succ = None

KEY = 811589153

with open(argv[1]) as f:
    original = [int(line.rstrip()) * KEY for line in f]

# turn into a circular linked list
head = Node(original[0])
cur = head
original_ptr = [head]
for i in range(1, len(original)):
    node = Node(original[i])
    node.pred = cur
    cur.succ = node
    cur = node
    original_ptr.append(node)
cur.succ = head
head.pred = cur

for round in range(1,11):
#    print('Round', round)
    for ptr in original_ptr:
        # if our value is 0, do nothing
        if ptr.val == 0:
            continue

        val = abs(ptr.val) % (len(original) - 1)
        if val == 0:
            continue
        elif ptr.val < 0:
            val = -val

        # remove ptr from the list
        ptr.pred.succ = ptr.succ
        ptr.succ.pred = ptr.pred

        # adjust head if necessary
        if ptr == head:
            head = ptr.succ if val > 0 else ptr.pred

        # find our new position
        new_ptr = ptr
        if val > 0:
            for _ in range(val):
                new_ptr = new_ptr.succ
        else:
            for _ in range(-val + 1):
                new_ptr = new_ptr.pred
        ptr.succ = new_ptr.succ
        new_ptr.succ.pred = ptr
        ptr.pred = new_ptr
        new_ptr.succ = ptr

    # cur = head
    # while (True):
    #     print(f'{cur.val} ', end='')
    #     cur = cur.succ
    #     if cur == head:
    #         print()
    #         break

# find 0 in the list
cur = head
while cur.val != 0:
    cur = cur.succ

tot = 0
for i in range(1,3001):
    cur = cur.succ
    if i % 1000 == 0:
        print(i, cur.val)
        tot += cur.val

print('Part 2:', tot)

