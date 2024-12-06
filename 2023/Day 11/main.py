from itertools import combinations

def find_galaxies(lines):
    galaxies = []

    for i, line in enumerate(lines):
        for j, char in enumerate(line):
            if char == '#':
                galaxies.append([i, j])

    return galaxies

def find_empty_space(lines):
    empty_lines = [i for i, line in enumerate(lines) if set(line) == {'.'}]
    empty_columns = []

    for j in range(len(lines[0])):
        if set([lines[i][j] for i in range(len(lines))]) == {'.'}:
            empty_columns.append(j)

    return empty_lines, empty_columns

def find_offset(galaxies, offset_distance, empty_lines, empty_columns):
    new_galaxies = list(galaxies)

    for galaxy in new_galaxies:
        offset_line = sum([offset_distance - 1 for line in empty_lines if line < galaxy[0]])
        offset_column = sum([offset_distance - 1 for column in empty_columns if column < galaxy[1]])
        galaxy[0] += offset_line
        galaxy[1] += offset_column

    return new_galaxies

def distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def part_one(lines):
    galaxies = find_galaxies(lines)
    new_galaxies = find_offset(galaxies, 2, *find_empty_space(lines))
    print("Part One Solution: " + str(sum([distance(*pair) for pair in combinations(new_galaxies, 2)])))

def part_two(lines):
    galaxies = find_galaxies(lines)
    new_galaxies = find_offset(galaxies, 1000000, *find_empty_space(lines))
    print("Part Two Solution: " + str(sum([distance(*pair) for pair in combinations(new_galaxies, 2)])))

if __name__ == '__main__':
    lines = [line.strip() for line in open('input.txt')]

    part_one(lines)
    part_two(lines)
