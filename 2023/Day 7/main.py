from collections import Counter

def part_one(hand):
	hand = hand.replace('J', 'X')
	return_hand = ['J23456789TXQKA'.index(i) for i in hand]
	ts = []
	for value in '23456789TQKA':
		count = Counter(hand.replace('J', value))
		sorted_counts = tuple(sorted(count.values()))
		types = [(1, 1, 1, 1, 1), (1, 1, 1, 2), (1, 2, 2), (1, 1, 3), (2, 3), (1, 4), (5, )].index(sorted_counts)
		ts.append(types)

	return (max(ts), return_hand)

def part_two(hand):
	return_hand = ['J23456789TXQKA'.index(i) for i in hand]
	ts = []
	for value in '23456789TQKA':
		count = Counter(hand.replace('J', value))
		sorted_counts = tuple(sorted(count.values()))
		types = [(1, 1, 1, 1, 1), (1, 1, 1, 2), (1, 2, 2), (1, 1, 3), (2, 3), (1, 4), (5, )].index(sorted_counts)
		ts.append(types)

	return (max(ts), return_hand)

if __name__ == '__main__':
	lines = open('input.txt').read().strip().split('\n')

	part_one_winnings = sorted((part_one(hand), int(value)) for hand, value in (line.split() for line in lines))
	part_one_total = 0

	for rank, (_, bid) in enumerate(part_one_winnings):
		part_one_total += rank * bid + bid

	print(part_one_total)

	part_two_winnings = sorted((part_two(hand), int(value)) for hand, value in (line.split() for line in lines))
	part_two_total = 0

	for rank, (_, bid) in enumerate(part_two_winnings):
		part_two_total += rank * bid + bid

	print(part_two_total)
