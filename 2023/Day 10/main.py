def part_one(grid, height, width):
    # Find the starting position 'S'
    start_x, start_y = -1, -1
    for x in range(height):
        for _ in range(width):
            if "S" in grid[x]:
                start_x = x
                start_y = grid[x].find("S")
                break

    # Define directions: right, down, left, up
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    valid_neighbors = ["-7J", "|LJ", "-FL", "|F7"]
    valid_directions = []
    
    # Check for valid directions from the starting point
    for i in range(4):
        direction = directions[i]
        next_x = start_x + direction[0]
        next_y = start_y + direction[1]
        
        if 0 <= next_x < height and 0 <= next_y < width and grid[next_x][next_y] in valid_neighbors[i]:
            valid_directions.append(i)

    # Pipe movement transformations based on current direction and pipe type
    direction_transform = {
        (0, "-"): 0,
        (0, "7"): 1,
        (0, "J"): 3,
        (2, "-"): 2,
        (2, "F"): 1,
        (2, "L"): 3,
        (1, "|"): 1,
        (1, "L"): 0,
        (1, "J"): 2,
        (3, "|"): 3,
        (3, "F"): 0,
        (3, "7"): 2,
    }

    current_direction = valid_directions[0]
    current_x = start_x + directions[current_direction][0]
    current_y = start_y + directions[current_direction][1]
    loop_length = 1

    loop_grid = [[0] * width for _ in range(height)]
    loop_grid[start_x][start_y] = 1  # mark the starting point

    # Traverse the loop and mark each tile
    while (current_x, current_y) != (start_x, start_y):
        loop_grid[current_x][current_y] = 1  # mark the current pipe in the loop
        loop_length += 1
        current_direction = direction_transform[(current_direction, grid[current_x][current_y])]
        current_x = current_x + directions[current_direction][0]
        current_y = current_y + directions[current_direction][1]
    
    print("Part One Solution: " + str(loop_length // 2))

def part_two(grid, height, width):
    loop_grid = [[0] * width for _ in range(height)]
    start_x, start_y = -1, -1
    
    # Find the starting position 'S'
    for x in range(height):
        for y in range(width):
            if "S" in grid[x]:
                start_x = x
                start_y = grid[x].find("S")

                break

    # Define directions: right, down, left, up
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    valid_neighbors = ["-7J", "|LJ", "-FL", "|F7"]
    valid_directions = []
    
    # Check for valid directions from the starting point
    for i in range(4):
        direction = directions[i]
        next_x = start_x + direction[0]
        next_y = start_y + direction[1]
        
        if 0 <= next_x < height and 0 <= next_y < width and grid[next_x][next_y] in valid_neighbors[i]:
            valid_directions.append(i)
    
    # Pipe movement transformations based on current direction and pipe type
    direction_transform = {
        (0, "-"): 0,
        (0, "7"): 1,
        (0, "J"): 3,
        (2, "-"): 2,
        (2, "F"): 1,
        (2, "L"): 3,
        (1, "|"): 1,
        (1, "L"): 0,
        (1, "J"): 2,
        (3, "|"): 3,
        (3, "F"): 0,
        (3, "7"): 2,
    }

    current_direction = valid_directions[0]
    current_x = start_x + directions[current_direction][0]
    current_y = start_y + directions[current_direction][1]
    loop_length = 1
    loop_grid[start_x][start_y] = 1  # mark the starting point

    # Traverse the loop and mark each tile
    while (current_x, current_y) != (start_x, start_y):
        loop_grid[current_x][current_y] = 1  # part 2
        loop_length += 1
        current_direction = direction_transform[(current_direction, grid[current_x][current_y])]
        current_x = current_x + directions[current_direction][0]
        current_y = current_y + directions[current_direction][1]

    # Count the enclosed tiles
    enclosed_tiles = 0
    for x in range(height):
        inside_loop = False

        for y in range(width):
            if loop_grid[x][y]:
                if grid[x][y] in "|JL" or (grid[x][y] == "S" and 3 in valid_directions):
                    inside_loop = not inside_loop
            else:
                if inside_loop:
                    enclosed_tiles += 1

    print("Part Two Solution: " + str(enclosed_tiles))

if __name__ == '__main__':
    grid = open('input.txt').read().split("\n")
    
    height = len(grid)
    width = len(grid[0])

    part_one(grid, height, width)
    part_two(grid, height, width)
