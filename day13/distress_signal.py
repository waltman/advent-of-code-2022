from sys import argv

with open(argv[1]) as f:
    for line in f:
        line = line.rstrip()
        if line:
            packet = eval(line)
            print(line)
            print(packet)
            print()
