def move_robot(warehouse_grid, position, direction):
    position += direction
    
    if all([warehouse_grid[position] != '[' or move_robot(warehouse_grid, position + 1, direction) and move_robot(warehouse_grid, position, direction),
            warehouse_grid[position] != ']' or move_robot(warehouse_grid, position - 1, direction) and move_robot(warehouse_grid, position, direction),
            warehouse_grid[position] != 'O' or move_robot(warehouse_grid, position, direction), warehouse_grid[position] != '#']):
                warehouse_grid[position], warehouse_grid[position - direction] = warehouse_grid[position - direction], warehouse_grid[position]

                return True
    
    return False

def simulate(warehouse_grid, moves):
    position = next((position for position in warehouse_grid if warehouse_grid[position] == '@'))

    for move in moves.replace('\n', ''):
        direction = {'<':-1, '>':1, '^':-1j, 'v':+1j}[move]
        copy = warehouse_grid.copy()

        if move_robot(warehouse_grid, position, direction): position += direction
        else: warehouse_grid = copy

    result = sum(position for position in warehouse_grid if warehouse_grid[position] in 'O[')
    
    return int(result.real + result.imag * 100)

def part_one(warehouse_grid, moves):
    print("Part One Solution: " + str(simulate({i + j * 1j: char for j, line in enumerate(warehouse_grid.split()) for i, char in enumerate(line)}, moves)))

def part_two(warehouse_grid, moves):
    warehouse_grid = warehouse_grid.translate(str.maketrans({'#':'##', '.':'..', 'O':'[]', '@':'@.'}))
    print("Part Two Solution: " + str(simulate({i + j * 1j: char for j, line in enumerate(warehouse_grid.split()) for i, char in enumerate(line)}, moves)))

if __name__ == '__main__':
    warehouse_grid, moves = open('input.txt').read().split('\n\n')

    part_one(warehouse_grid, moves)
    part_two(warehouse_grid, moves)
