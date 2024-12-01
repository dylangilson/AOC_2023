from functools import reduce
from math import gcd

def part_one():
	steps = 0
	start = 'AAA'
	
	while start != 'ZZZ':
		for direction in lines:
			if direction == 'L':
				start = left[a.index(start)]
			else:
				start = right[a.index(start)]

			steps += 1

	print("Part One Solution: " + str(steps))

def lcm(a, b):
	return a * b // gcd(a, b)

def part_two():
	nodes = [i for i in a if i[2]=='A']
	steps = 0
	count_z = 0
	lengths = []
	length = len(nodes)

	while count_z < length:
		for direction in lines:
			for i in range(len(nodes)): 
				if direction == 'L':
					nodes[i] = left[a.index(nodes[i])]
				else:
					nodes[i] = right[a.index(nodes[i])]

			steps += 1

			for node in nodes:
				if node[2] == 'Z':
					count_z += 1

					nodes.remove(node)
					lengths.append(steps)

	print("Part Two Solution: " + str(reduce(lcm, lengths)))
	
if __name__ == '__main__':
	lines, network = open('input.txt').read().split('\n\n')
	network = network.split('\n')

	a = [i[0:3] for i in network]
	left = [i[7:10] for i in network]
	right = [i[12:15] for i in network]

	part_one()
	part_two()
