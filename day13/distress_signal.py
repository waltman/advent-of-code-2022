from sys import argv

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
    index = 1
    for line in f:
        line = line.rstrip()
        if line:
            packets.append(eval(line))
            if len(packets) == 2:
#                print(f'comparing {packets[0]} and {packets[1]}')
                res = right_order(packets[0], packets[1])
                # print('result:', res)
                # packets = []
                if right_order(packets[0], packets[1]) == 1:
                    index_sum += index
                index += 1
                packets = []

print('Part 1:', index_sum)
