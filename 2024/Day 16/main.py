from collections import defaultdict
from heapq import heappop, heappush

# solve the maze input using djikstra's algorithm for shortest path
def solve_maze(maze, visited):
    start_position = next(position for position in maze if maze[position] == 'S')
    best_score = float('inf')
    distances = defaultdict(lambda: float('inf'))
    turn_count = 0
    priority_queue = [(0, turn_count, start_position, 1j, [start_position])]
    rotation_cost = 1001

    while priority_queue:
        score, _, position, direction, path = heappop(priority_queue)

        if score > distances[position, direction]: continue
        else: distances[position, direction] = score

        if maze[position] == 'E' and score <= best_score:
            visited += path
            best_score = score

        for rotation, cost in (1, 1), (+1j, rotation_cost), (-1j, rotation_cost):
            cost = score + cost
            turn_count = turn_count + 1
            next_position = position + direction * rotation
            next_direction = direction * rotation

            if next_position not in maze: continue

            heappush(priority_queue, (cost, turn_count, next_position, next_direction, path + [next_position]))

    return best_score

def part_one(maze, visited):
    print("Part One Solution: " + str(solve_maze(maze, visited)))

def part_two(visited):
    print("Part Two Solution: " + str(len(set(visited))))

if __name__ == '__main__':
    maze = {i + j * 1j: char for i, line in enumerate(open('input.txt')) for j, char in enumerate(line) if char != '#'}
    visited = []

    part_one(maze, visited)
    part_two(visited)
