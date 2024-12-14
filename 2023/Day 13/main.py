def find_reflection_line(pattern, type):
    for row_index in range(len(pattern)):
        if sum(char1 != char2 for top_row, bottom_row in zip(pattern[row_index - 1::-1], pattern[row_index:]) for char1, char2 in zip(top_row, bottom_row)) == type:
            return row_index

    return 0

def part_one(patterns, type):
    print("Part One Solution: " + str(sum(find_reflection_line(pattern, type) * 100 + find_reflection_line([*zip(*pattern)], type) for pattern in patterns)))

def part_two(patterns, type):
    print("Part Two Solution: " + str(sum(find_reflection_line(pattern, type) * 100 + find_reflection_line([*zip(*pattern)], type) for pattern in patterns)))

if __name__ == '__main__':
    patterns = [pattern.splitlines() for pattern in open('input.txt').read().split('\n\n')]

    part_one(patterns, 0) # 0 -> horizontal reflection
    part_two(patterns, 1) # 1 -> vertical reflection
