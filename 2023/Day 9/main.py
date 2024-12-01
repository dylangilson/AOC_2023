from math import factorial

# Calculate binomial coefficient using the factorial formula
def comb(n, k):
    if k > n:
        return 0
    
    if k == 0 or k == n:
        return 1
    
    return factorial(n) // (factorial(k) * factorial(n - k))

# Lagrange function
def part_one(y_values):
    result = 0 

    for values in y_values:
        num_points = len(values)

        for i, y_value in enumerate(values):
            # comb(num_points, i) is the binomial coefficient C(num_points, i)
            # (-1)**(num_points - 1 - i) alternates signs based on the index
            result += y_value * comb(num_points, i) * (-1)**(num_points - 1 - i)
    
    print("Part One Solution: " + str(result))

# Lagrange function
def part_two(y_values):
    result = 0

    for values in y_values:
        num_points = len(values)

        for i, y_value in enumerate(values):
            # comb(num_points, i + 1) is the binomial coefficient C(num_points, i + 1)
            # (-1)**(i) alternates signs based on the index
            result += y_value * comb(num_points, i + 1) * (-1)**(i)

    print("Part Two Solution: " + str(result))

if __name__ == '__main__':
    lines = open('input.txt').read().strip().splitlines()
    y_values = []

    for line in lines:
        y_values.append(list(map(int, line.split())))

    part_one(y_values)
    part_two(y_values)
