from functools import lru_cache

@lru_cache(maxsize=None)
def recurse(lava, springs):
    result = 0

    if not springs: return '#' not in lava
    
    current, springs = springs[0], springs[1:]

    for i in range(len(lava) - sum(springs) - len(springs) - current + 1):
        if '#' in lava[:i]: break

        next = i + current

        if next <= len(lava) and '.' not in lava[i : next] and lava[next : next + 1] != '#': result += recurse(lava[next + 1:], springs)

    return result

def part_one(lines):
    print('Part One Solution: ' + str(sum(recurse(lava, tuple(map(int, springs.split(',')))) for (lava, springs) in lines)))

def part_two(lines):
    print('Part Two Solution: ' + str(sum(recurse('?'.join([lava] * 5), tuple(map(int, springs.split(','))) * 5) for (lava, springs) in lines)))

if __name__ == '__main__':
    lines = [line.split() for line in open('input.txt').read().splitlines()]

    part_one(lines)
    part_two(lines)
