from sys import argv
import functools

def right_order(left, right):
    if type(left) == int and type(right) == int:
        if left < right:
            return 1
        elif left == right:
            return 0
        else:
            return -1
    for i in range(len(left)):
        if i >= len(right):
            return -1
        else:
            lval = left[i]
            rval = right[i]
            if (type(lval) == int and type(rval) == int) or (type(lval) == list and type(rval) == list):
                if (res := right_order(lval, rval)) in [-1, 1]:
                    return res
            elif type(lval) == int:
                if (res := right_order([lval], rval)) in [-1,1]:
                    return res
            else:
                if (res := right_order(lval, [rval])) in [-1,1]:
                    return res
    return 1 if len(left) < len(right) else 0

index_sum = 0
with open(argv[1]) as f:
    packets = []
    all_packets = []
    index = 1
    for line in f:
        line = line.rstrip()
        if line:
            packets.append(eval(line))
            all_packets.append(packets[-1])
            if len(packets) == 2:
                res = right_order(packets[0], packets[1])
                if right_order(packets[0], packets[1]) == 1:
                    index_sum += index
                index += 1
                packets = []

print('Part 1:', index_sum)
all_packets.append([[2]])
all_packets.append([[6]])
sorted_packets = sorted(all_packets, key=functools.cmp_to_key(right_order))[::-1]
product = 1
for i in range(len(sorted_packets)):
    if sorted_packets[i] in [[[2]], [[6]]]:
        product *= i+1
print('Part 2:', product)
