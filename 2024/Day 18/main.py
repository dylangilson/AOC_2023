from collections import deque

def bfs(grid, start, end):
    rows, cols = len(grid), len(grid[0])
    queue = deque([start])
    distances = [[-1] * cols for _ in range(rows)]
    distances[start[0]][start[1]] = 0
    directions = [(-1, 0), (0, -1), (0, 1), (1, 0)]
    
    while queue:
        x, y = queue.popleft()
        
        if (x, y) == end: return distances[x][y]
        
        for dx, dy in directions:
            nx = x + dx
            ny = y + dy
            
            if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == '.' and distances[nx][ny] == -1:
                distances[nx][ny] = distances[x][y] + 1
                queue.append((nx, ny))
    
    return -1

def simulate_bytes(falling_bytes, grid_size):
    grid = [['.' for _ in range(grid_size)] for _ in range(grid_size)]

    for byte in falling_bytes:
        if 0 <= byte[0] < grid_size and 0 <= byte[1] < grid_size: grid[byte[0]][byte[1]] = '#'
    
    return grid

def simulate(falling_bytes, bytes_to_simulate, grid_size):
    start = (0, 0)
    end = (grid_size, grid_size)
    grid = simulate_bytes(falling_bytes[:bytes_to_simulate], grid_size + 1)

    return bfs(grid, start, end)

def part_one(falling_bytes, bytes_to_simulate, grid_size):
    print('Part One Solution: ' + str(simulate(falling_bytes, bytes_to_simulate, grid_size)))

def find_first_path_block(falling_bytes, grid_size):
    start = (0, 0)
    end = (grid_size, grid_size)
    
    for i in range(len(falling_bytes)):
        grid = simulate_bytes(falling_bytes[:i + 1], grid_size + 1)
        if bfs(grid, start, end) == -1: return falling_bytes[i]

    return None

def part_two(falling_bytes, grid_size):
    print(f"Part Two Solution: {','.join(map(str, find_first_path_block(falling_bytes, grid_size)))}")

if __name__ == '__main__':
    falling_bytes = [tuple(map(int, line.strip().split(','))) for line in open('input.txt')]
    bytes_to_simulate = 1024
    grid_size = 70
    
    part_one(falling_bytes, bytes_to_simulate, grid_size)
    part_two(falling_bytes, grid_size)
