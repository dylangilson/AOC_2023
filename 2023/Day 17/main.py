from heapq import heappop, heappush

def calculate_minimum_heat_loss(lines, min_steps, max_steps):
    destination = [*lines][-1]
    path_queue = [(0, 0, 0, 1), (0, 0, 0, 1j)]  # (heat_loss, steps_taken, position, direction)
    visited = set()
    counter = 0

    while path_queue:
        current_heat_loss, _, position, direction = heappop(path_queue)

        if position == destination: return current_heat_loss
        if (position, direction) in visited: continue

        visited.add((position, direction))

        for turn_direction in (1j / direction, -1j / direction):
            for step in range(min_steps, max_steps + 1):
                new_position = position + turn_direction * step

                if new_position in lines:
                    heat_loss_from_move = sum(lines[position + turn_direction * j] for j in range(1, step + 1))
                    counter += 1

                    heappush(path_queue, (current_heat_loss + heat_loss_from_move, counter, new_position, turn_direction))

def part_one(lines):
    print("Part One Solution: " + str(calculate_minimum_heat_loss(lines, 1, 3)))

def part_two(lines):
    print("Part Two Solution: " + str(calculate_minimum_heat_loss(lines, 4, 10)))

if __name__ == '__main__':
    lines = {i + j * 1j: int(char) for j, line in enumerate(open('input.txt')) for i, char in enumerate(line.strip())}

    part_one(lines)
    part_two(lines)
