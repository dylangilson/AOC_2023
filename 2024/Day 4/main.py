def part_one(dictionary):
    result = 0
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    for position, value in dictionary.items():
        if value == 'X':
            for direction in directions:
                current = position

                for i, char in enumerate(['M', 'A', 'S']):
                    current = (current[0] + direction[0], current[1] + direction[1])

                    if current not in dictionary or dictionary[current] != char:
                        break
                    if i == 2 and dictionary[current] == 'S':
                        result += 1

    print("Part One Solution: " + str(result))

def part_two(dictionary):
    result = 0
    directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]

    for position, value in dictionary.items():
        if value == 'A':
            m_counter = s_counter = 0
            top_left = bottom_right = None

            for direction in directions:
                current = (position[0] + direction[0], position[1] + direction[1])

                if current not in dictionary:
                    break

                if dictionary[current] == 'M': m_counter += 1
                if dictionary[current] == 'S': s_counter += 1
                if direction == (1, 1): top_left = dictionary[current]
                if direction == (-1, -1): bottom_right = dictionary[current]

            if m_counter == s_counter == 2 and top_left != bottom_right:
                result +=1

    print("Part Two Solution: " + str(result))

if __name__ == '__main__':
    lines = open('input.txt').read().strip().splitlines()
    dictionary = {(i, j): char for i, line in enumerate(lines) for j, char in enumerate(line)}

    part_one(dictionary)
    part_two(dictionary)
