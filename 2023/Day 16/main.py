def simulate(lines, directions):
    energized_positions = set()

    while directions:
        position, direction = directions.pop()

        while (position, direction) not in energized_positions:
            energized_positions.add((position, direction))
            position += direction
            tile = lines.get(position)

            if tile == '|':
                direction = 1j
                directions.append((position, -direction))
            elif tile == '-':
                direction = -1
                directions.append((position, -direction))
            elif tile == '/':
                direction = -complex(direction.imag, direction.real)
            elif tile == '\\':
                direction = complex(direction.imag, direction.real)
            elif tile is None:
                break

    return len(set(position for position, _ in energized_positions)) - 1

def part_one(lines):
    print('Part One Solution: ' + str(simulate(lines, [(-1, 1)])))

def part_two(lines):
    print('Part Two Solution: ' + str(max(map(lambda instructions: simulate(lines, instructions), 
                                    ([(position - direction, direction)] for direction in (1, 1j, -1, -1j) for position in lines if position - direction not in lines)))))

if __name__ == '__main__':
    lines = {i + j * 1j: char for j, line in enumerate(open('input.txt')) for i, char in enumerate(line.strip())}

    part_one(lines)
    part_two(lines)
