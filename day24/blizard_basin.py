from sys import argv

entrance = (0,1)
with open(argv[1]) as f:
    row = 0
    for line in f:
        if row > 0:
            if line[0:2] == '##': # last row
                num_rows = row + 1
                num_cols = len(line) - 2
                goal = (row, num_cols-1)
                break
        row += 1

print(num_rows, num_cols, goal)

            
            
