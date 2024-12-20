def part_one(unique_regions):
    print("Part One Solution: " + 
          str(sum(len(region) * len({(position, direction) for direction in (1, -1, 1j, -1j) for position in region if position + direction not in region}) for region in unique_regions)))

def part_two(unique_regions):
    result = 0

    for region in unique_regions:
        exposed_sides = {(position, direction) for direction in (+1, -1, +1j, -1j) for position in region if position + direction not in region}
        result += len(region) * len(exposed_sides - {(p + direction * 1j, direction) for p, direction in exposed_sides})

    print("Part Two Solution: " + str(result))

if __name__ == '__main__':
    lines = {i + j * 1j: char for i, line in enumerate(open('input.txt')) for j, char in enumerate(line.strip())}
    regions = {position: {position} for position in lines}

    # merge neighbouring regions that have the same plant type
    for position in lines:
        for neighbor in position + 1, position - 1, position + 1j, position - 1j:
            if neighbor in lines and lines[position] == lines[neighbor]:
                regions[position] |= regions[neighbor]
                for neighbor_position in regions[position]: 
                    regions[neighbor_position] = regions[position]

    unique_regions = {tuple(region) for region in regions.values()}

    part_one(unique_regions)
    part_two(unique_regions)
