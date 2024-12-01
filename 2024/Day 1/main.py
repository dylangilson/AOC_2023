def part_one(left, right):
    distance = 0

    for i in range(len(left)):
        distance += abs(left[i] - right[i])
    
    print("Part One Solution: " + str(distance))

def part_two(left, right):
    similarity_score = 0

    for element in left:
        similarity_score += element * right.count(element)

    print("Part Two Solution: " + str(similarity_score))

if __name__ == '__main__':
    lines = open('input.txt').read().strip().split('\n')
    
    left = []
    right = []

    for line in lines:
        line = line.split()
        left.append(int(line[0]))
        right.append(int(line[1]))

    left = sorted(left)
    right = sorted(right)

    part_one(left, right)
    part_two(left, right)
