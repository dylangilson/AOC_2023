from functools import lru_cache

@lru_cache(None)
def count_combinations(patterns, design):
    if design == '': return 1
    
    return sum(count_combinations(patterns, design[len(pattern):]) for pattern in patterns.split(', ') if design.startswith(pattern))

def part_one(patterns, designs):
    print(sum([bool(count_combinations(patterns, design)) for design in designs]))

def part_two(patterns, designs):
    print(sum([int(count_combinations(patterns, design)) for design in designs]))

if __name__ == '__main__':
    patterns, _, *designs = open('input.txt').read().splitlines()

    part_one(patterns, designs)
    part_two(patterns, designs)
