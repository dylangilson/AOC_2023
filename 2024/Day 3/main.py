import re

pattern_one = r'mul\((\d{1,3}),(\d{1,3})\)'
pattern_two = r'mul\(\d{1,3},\d{1,3}\)|do\(\)|don\'t\(\)'

def part_one(lines):
    muls = re.findall(pattern_one, lines)
    print("Part One Solution: " + str(sum(int(x) * int(y) for x, y in muls)))

def part_two(lines):
    instructions = re.findall(pattern_two, lines)
    muls = re.findall(pattern_one, lines)
    terms = [(int(x) * int(y)) for x, y in muls]
    enabled = True
    result = index = 0

    for instruction in instructions:
        if 'do()' in instruction:
            enabled = True
        elif "don't()" in instruction:
            enabled = False
        else:
            result += terms[index] if enabled else 0
            index += 1
    
    print("Part Two Solution: " + str(result))

if __name__ == '__main__':
    lines = open('input.txt').read().strip()

    part_one(lines)
    part_two(lines)
