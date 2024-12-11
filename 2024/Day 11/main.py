from collections import defaultdict

def blink(stone_count):
    new_stone_count = defaultdict(int)
    
    for stone, count in stone_count.items():
        if stone == 0: new_stone_count[1] += count
        else:
            string = str(stone)

            if len(string) % 2 == 0:
                middle = len(string) // 2
                new_stone_count[int(string[:middle])] += count
                new_stone_count[int(string[middle:])] += count
            else: new_stone_count[stone * 2024] += count
    
    return new_stone_count

def part_one(stones):
    stone_count = defaultdict(int)

    for stone in stones:
        stone_count[stone] += 1

    for _ in range(25):
        stone_count = blink(stone_count)

    print("Part One Solution: " + str(sum(stone_count.values())))

def part_two(stones):
    stone_count = defaultdict(int)

    for stone in stones:
        stone_count[stone] += 1
    
    for _ in range(75):
        stone_count = blink(stone_count)

    print("Part Two Solution: " + str(sum(stone_count.values())))

if __name__ == '__main__':
    stones = [int(char) for line in open('input.txt').read().strip().splitlines() for char in line.split()]

    part_one(stones)
    part_two(stones)
