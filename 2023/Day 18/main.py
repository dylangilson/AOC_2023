def calculate_lava_volume(instructions):
    position = 0
    volume = 1

    for (dx, dy), steps in instructions:
        position += dx * steps
        volume += dy * steps * position + steps / 2

    return int(volume)

def part_one(lines, direction_map):
    print('Part One Solution: ' + str(calculate_lava_volume(((direction_map[direction], int(steps)) for direction, steps, _ in lines))))

def part_two(lines, direction_map):
    print('Part Two Solution: ' + str(calculate_lava_volume(((direction_map[edge_color[7]], int(edge_color[2:7], 16)) for _, _, edge_color in lines))))

if __name__ == '__main__':
    lines = list(map(str.split, open('input.txt')))
    direction_map = {'R': (1, 0), 'D': (0, 1), 'L': (-1, 0), 'U': (0, -1), '0': (1, 0), '1': (0, 1), '2': (-1, 0), '3': (0, -1)}

    part_one(lines, direction_map)
    part_two(lines, direction_map)
