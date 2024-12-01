if __name__ == "__main__":
    file = open("input.txt")
    lines = file.readlines()

    part_one_total = 0
    tickets = [1 for _ in lines]

    for index, line in enumerate(lines):
        line = line.split(':')[1]
        lucky_numbers, our_numbers = line.split('|')
        lucky_numbers = lucky_numbers.split()
        our_numbers = our_numbers.split()
        wins = len(set(lucky_numbers) & set(our_numbers))

        if wins > 0:
            part_one_total += 2 ** (wins - 1)

        for i in range(wins):
            tickets[index + i + 1] += tickets[index]

    print(part_one_total)

    part_two_total = sum(tickets)

    print(part_two_total)
