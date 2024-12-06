from collections import defaultdict
from functools import cmp_to_key

def is_update_ordered(order_dictionary, update):
    update = update.split(',')

    for i in range(len(update)):
        for j in range(i + 1, len(update)):
            if update[j] not in order_dictionary.get(update[i], []):
                return 0
                
    return int(update[len(update) // 2])

def part_one(order_dictionary, updates):       
    print("Part One Solution: " + str(sum(is_update_ordered(order_dictionary, update) for update in updates)))

def part_two(updates, cmp):
    print("Part Two Solution: " + 
          str(sum(int(sorted(update.split(','), key=cmp)[len(update.split(',')) // 2]) for update in updates if update.split(',') != sorted(update.split(','), key=cmp))))

if __name__ == '__main__':
    lines = open('input.txt').read().strip().splitlines()
    rules, updates = lines[:lines.index('')], lines[lines.index('') + 1:]
    order_dictionary = defaultdict(list)
    
    for rule in rules:
        x, y = rule.split('|')
        order_dictionary[x].append(y)

    cmp = cmp_to_key(lambda x, y: -(x + '|' + y in rules))

    part_one(order_dictionary, updates)
    part_two(updates, cmp)
