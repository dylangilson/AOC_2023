def move_blocks(line):
    disk = [int(i / 2) if i % 2 == 0 else None for i, char in enumerate(line) for _ in range(int(char))]

    for i in range(len(disk) - 1, -1, -1):
        if disk[i] is None: continue

        for j in range(i):
            if disk[j] is None:
                disk[j], disk[i] = disk[i], None
                break

    return disk

def part_one(line):
    print("Part One Solution: " + str(sum(i * id for i, id in enumerate(move_blocks(line)) if id is not None)))

def move_files(line):
    disk = [(int(i / 2), int(char)) if i % 2 == 0 else (None, int(char)) for i, char in enumerate(line)]

    for id in range(disk[-1][0], -1, -1):
        for i in range(len(disk)):
            i_id, i_len = disk[i]

            if i_id == id: break

        for j in range(i):
            j_id, empty_blocks = disk[j]

            if j_id is not None: continue

            if i_len <= empty_blocks:
                remaining = empty_blocks - i_len
                disk[j] = disk[i]
                disk[i] = (None, i_len)

                if remaining:
                    disk = disk[:j + 1] + [(None, remaining)] + disk[j + 1:]
                
                break

    result = []

    for id, length in disk:
        result.extend([id] * length)
    
    return result

def part_two(line):
    print("Part Two Solution: " + str(sum(i * id for i, id in enumerate(move_files(line)) if id is not None)))

if __name__ == '__main__':
    line = open('input.txt').read().strip()

    part_one(line)
    part_two(line)
