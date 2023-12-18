import re

if __name__ == "__main__":
    file = open("input.txt")
    lines = file.readlines()

    num_rows = len(lines)
    num_columns = len(lines[0]) - 1

    symbols = {(i, j): [] for i in range(num_rows) for j in range(num_columns) if lines[i][j] not in '0123456789.'}
    
    for r, row in enumerate(lines):
        for n in re.finditer(r'\d+', row):
            edge = {(i, j) for i in (r - 1, r, r + 1) for j in range(n.start() - 1, n.end() + 1)}

            for i in edge & symbols.keys():
                symbols[i].append(int(n.group()))
    
    total_part_one = sum(sum(index) for index in symbols.values())

    total_part_two = 0
    for index in symbols.values():
        if len(index) == 2:
            product = 1

            for x in index:
                product *= x

            total_part_two += product

    print(total_part_two)        
