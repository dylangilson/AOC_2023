from itertools import cycle
from copy import deepcopy

def part_one(lines):
    result = 1
    directions = cycle([(-1, 0), (0, 1), (1, 0), (0, -1)])
    direction = next(directions)
    position = next(((i, j) for i in range(len(lines)) for j in range(len(lines[0])) if lines[i][j] == '^'), None)

    while 0 <= position[0] + direction[0] < len(lines) and 0 <= position[1] + direction[1] < len(lines[0]):
        next_position = tuple(a + b for a, b in zip(position, direction))

        if lines[next_position[0]][next_position[1]] == '.' or lines[next_position[0]][next_position[1]] == 'X' or lines[next_position[0]][next_position[1]] == '^':
            if lines[next_position[0]][next_position[1]] == '.': result += 1

            position = next_position
            lines[position[0]] = lines[position[0]][:position[1]] + 'X' + lines[position[0]][position[1] + 1:]
        else:
            direction = next(directions)

    print("Part One Solution: " + str(result))

def part_two(lines):
    result = 0
    directions = cycle([(-1, 0), (0, 1), (1, 0), (0, -1)])
    direction = next(directions)
    position = next(((i, j) for i in range(len(lines)) for j in range(len(lines[0])) if lines[i][j] == '^'), None)
    original_position = position
    original_visited_positions = set()
    original_visited_positions.add(position)

    while 0 <= position[0] + direction[0] < len(lines) and 0 <= position[1] + direction[1] < len(lines[0]):
        next_position = tuple(a + b for a, b in zip(position, direction))

        if lines[next_position[0]][next_position[1]] == '.' or lines[next_position[0]][next_position[1]] == 'X' or lines[next_position[0]][next_position[1]] == '^':
            position = next_position
            original_visited_positions.add(position)
        else:
            direction = next(directions)

    while direction != (-1, 0): direction = next(directions)

    for visit in original_visited_positions:
        temp_lines = deepcopy(lines)
        temp_position = deepcopy(original_position)

        temp_lines[visit[0]] = temp_lines[visit[0]][:visit[1]] + '#' + temp_lines[visit[0]][visit[1] + 1:]
        visited_positions = set()
        loop = False

        while 0 <= temp_position[0] + direction[0] < len(lines) and 0 <= temp_position[1] + direction[1] < len(lines[0]):
            next_position = tuple(a + b for a, b in zip(temp_position, direction))

            if (next_position, direction) in visited_positions:
                loop = True
                breakcd

            visited_positions.add((next_position, direction))

            if temp_lines[next_position[0]][next_position[1]] == '.' or temp_lines[next_position[0]][next_position[1]] == 'X' or temp_lines[next_position[0]][next_position[1]] == '^':
                temp_position = next_position
                temp_lines[temp_position[0]] = temp_lines[temp_position[0]][:temp_position[1]] + 'X' + temp_lines[temp_position[0]][temp_position[1] + 1:]
            else:
                direction = next(directions)

        if loop: result += 1

        while direction != (-1, 0): direction = next(directions)

    print("Part Two Solution: " + str(result))

if __name__ == '__main__':
    lines = open('input.txt').read().strip().splitlines()

    part_one(deepcopy(lines))
    part_two(lines)
