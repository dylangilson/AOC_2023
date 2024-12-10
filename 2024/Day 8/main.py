def part_one(lines, antinodes, a, b):
    x = b[0] + b[0] - a[0]
    y = b[1] + b[1] - a[1]

    if 0 <= x < len(lines) and 0 <= y < len(lines[0]): antinodes.add((x,y))

def part_two(lines, antinodes, a, b):
    antinodes.add((b[0], b[1]))

    x = b[0] + b[0] - a[0]
    y = b[1] + b[1] - a[1]

    while 0 <= x < len(lines) and 0 <= y < len(lines[0]):
        antinodes.add((x, y))

        x += b[0] - a[0]
        y += b[1] - a[1]

def find_antinodes(lines):
    antinodes = set()
    antinodes2 = set()
    nodes = {}

    for i in range(len(lines)):
        for j in range(len(lines[0])):
            if lines[i][j] != '.':
                if lines[i][j] in nodes:
                    nodes[lines[i][j]].append((i, j))
                else:
                    nodes[lines[i][j]] = [(i, j)]

    for i in nodes:
        for j in range(len(nodes[i])):
            for k in range(j):
                a = nodes[i][j]
                b = nodes[i][k]

                part_one(lines, antinodes, a, b)
                part_one(lines, antinodes, b, a)
                part_two(lines, antinodes2, a, b)
                part_two(lines, antinodes2, b, a)

    print("Part One Solution: " + str(len(antinodes)))
    print("Part Two Solution: " + str(len(antinodes2)))

if __name__ == '__main__':
    lines = open('input.txt').read().strip().splitlines()

    find_antinodes(lines)
