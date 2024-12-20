from collections import defaultdict

def hash(str):
    hash_value = 0

    for char in str:
        hash_value += ord(char)
        hash_value = 17 * hash_value % 256

    return hash_value

def part_one(data):
    print('Part One Solution: ' + str(sum(hash(char) for char in data)))

def hashmap(data):
    boxes = defaultdict(dict)

    for operation in data:
        if '-' in operation:
            label = operation[:-1]
            boxes[hash(label)].pop(label, None)
        else:
            label, i = operation.split('=')
            boxes[hash(label)][label] = int(i)

    return boxes

def part_two(data):
    boxes = hashmap(data)
    print('Part Two Solution: ' + str(sum((i + 1) * (j + 1) * value for i in boxes for j, value in enumerate(boxes[i].values()))))

if __name__ == '__main__':
    data = open('input.txt').read().strip().split(',')

    part_one(data)
    part_two(data)
