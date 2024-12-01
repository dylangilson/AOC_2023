from functools import reduce

def part_one(times, distances):
	total = 1
	totals = [0] * len(times)

	for i in range(len(times)):
		for x in range(times[i] + 1):
			dx = x * (times[i] - x)
			
			if dx > distances[i]:
				totals[i] += 1

		total *= totals[i]
	
	return total

def part_two(time, distance):
	total = 0

	for x in range(time + 1):
		dx = x * (time - x)

		if dx > distance:
			total += 1

	return total

if __name__ == '__main__':
	lines = open('input.txt').read().strip().split('\n')
	times = [int(x) for x in lines[0].split(':')[1].split()]
	distances = [int(x) for x in lines[1].split(':')[1].split()]

	part_one_total = part_one(times, distances)
	print(part_one_total)

	time = int(reduce(lambda x, y: x + y, map(str, times)))
	distance = int(reduce(lambda x, y: x + y, map(str, distances)))

	part_two_total = part_two(time, distance)
	print(part_two_total)
