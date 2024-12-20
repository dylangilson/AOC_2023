import re

def calculate_quadrant_product(seconds):
    result = [0, 0, 0, 0]

    for position_x, position_y, velocity_x, velocity_y in robots_data:
        current_x = (position_x + velocity_x * seconds) % width
        current_y = (position_y + velocity_y * seconds) % height

        result[0] += current_x > width // 2 and current_y > height // 2
        result[1] += current_x > width // 2 and current_y < height // 2
        result[2] += current_x < width // 2 and current_y > height // 2
        result[3] += current_x < width // 2 and current_y < height // 2

    return result[0] * result[1] * result[2] * result[3]

if __name__ == '__main__':
    robots_data = [[*map(int, re.findall(r'-?\d+', line))] for line in open('input.txt')]
    width = 101
    height = 103
    max_seconds = 10000

    print("Part One Solution: " + str(calculate_quadrant_product(100)))
    print("Part Two Solution: " + str(min(range(max_seconds), key=calculate_quadrant_product)))
