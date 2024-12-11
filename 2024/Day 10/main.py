def dfs_visited(lines, visited, x, y):
    result = 0
    directions = [(-1, 0), (0, -1), (0, 1), (1, 0)]

    if (x, y) in visited: return 0
    
    visited.add((x, y))

    if lines[x][y] == 9: return 1

    for i, j in directions:
        dx, dy = x + i, y + j

        if dx in range(len(lines)) and dy in range(len(lines[0])):
            if lines[dx][dy] == lines[x][y] + 1:
                result += dfs_visited(lines, visited, dx, dy)

    return result

def part_one(lines):
    print("Part One Solution: " + str(sum(dfs_visited(lines, set(), i, j) for i in range(len(lines)) for j in range(len(lines[0])) if lines[i][j] == 0)))

def dfs(lines, x, y):
    result = 0
    directions = [(-1, 0), (0, -1), (0, 1), (1, 0)]

    if lines[x][y] == 9: return 1

    for i, j in directions:
        dx, dy = x + i, y + j

        if dx in range(len(lines)) and dy in range(len(lines[0])):
            if lines[dx][dy] == lines[x][y] + 1: result += dfs(lines, dx, dy)

    return result

def part_two(lines):
    print("Part Two Solution: " + str(sum(dfs(lines, i, j) for i in range(len(lines)) for j in range(len(lines[0])) if lines[i][j] == 0)))

if __name__ == '__main__':
    lines = [list(map(int, char)) for char in open('input.txt').read().strip().splitlines()]

    part_one(lines)
    part_two(lines)
