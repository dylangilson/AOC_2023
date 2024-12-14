import re

def rotate_90(lines):
    return [''.join(row) for row in zip(*lines[::-1])]

def one_cycle(lines):   
    return [re.sub(r'[.O]+', lambda m: ''.join(sorted(m[0])[::-1]), row) for row in rotate_90(lines)]

def part_one(lines):
    print('Part One Solution: ' + str(sum(i for row in one_cycle(rotate_90(rotate_90(lines))) for i, cell in enumerate(row[::-1], 1) if cell == 'O')))

def overload(lines):
    cache = {}
    n = 1_000_000_000

    for r in range(n):
        lines = tuple(one_cycle(one_cycle(one_cycle(one_cycle(lines)))))
        s = cache.get(lines, 0)

        if s: return cache[(n - s) % (r - s) + (s - 1)]

        cache.update({lines:r, r:sum(i for row in rotate_90(lines) for i, cell in enumerate(row[::-1], 1) if cell == 'O')})

def part_two(lines):
    print("Part Two Solution: " + str(overload(rotate_90(rotate_90(lines)))))

if __name__ == '__main__':
    lines = open('input.txt').read().splitlines()

    part_one(lines)
    part_two(lines)
