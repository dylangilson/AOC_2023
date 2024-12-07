from itertools import product

def evaluate(expression):
    result = expression[0]

    for i in range(1, len(expression), 2):
        operator = expression[i]
        value = expression[i + 1]

        if operator == '+': result += value
        elif operator == '*': result *= value
        elif operator == '||': result = int(str(result) + str(value))

    return result

def part_one(equations):
    solution = 0
    operators = ['+', '*']

    for target, values in equations:
        for combinations in product(operators, repeat=len(values) - 1):
            expression = [values[i] for i in range(len(values))]
            [expression.insert(i * 2 + 1, operator) for i, operator in enumerate(combinations)]

            result = evaluate(expression)

            if result == target: 
                solution += result
                break

    print("Part One Solution: " + str(solution))

def part_two(equations):
    solution = 0
    operators = ['+', '*', '||']

    for target, values in equations:
        for combinations in product(operators, repeat=len(values) - 1):
            expression = [values[i] for i in range(len(values))]
            [expression.insert(i * 2 + 1, operator) for i, operator in enumerate(combinations)]
 
            result = evaluate(expression)

            if result == target: 
                solution += result
                break

    print("Part Two Solution: " + str(solution))

if __name__ == '__main__':
    equations = [(int(result), [int(value.strip()) for value in values.split(' ') if value.strip()]) 
                 for line in open('input.txt').read().strip().splitlines() for result, values in [line.split(':')]]

    part_one(equations)
    part_two(equations)
