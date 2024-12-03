def safe(line):
    for i in range(len(line) - 1):
        if not 1 <= line[i] - line[i + 1] <= 3:
            return False
        
    return True

def safe_exception(line):
    for i in range(len(line) - 1):
        if not 1 <= line[i] - line[i + 1] <= 3:
            return any(safe(line[j - 1:j] + line[j + 1:]) for j in (i, i + 1))
        
    return True

def part_one(lines):
    print("Part One Solution: " + str((sum(safe(line) or safe(line[::-1]) for line in lines))))

def part_two(lines):
    print("Part Two Solution: " + str((sum(safe_exception(line) or safe_exception(line[::-1]) for line in lines))))

if __name__ == '__main__':
    lines = [list(map(int, line.split())) for line in open('input.txt').read().strip().split('\n')]

    part_one(lines)
    part_two(lines)
