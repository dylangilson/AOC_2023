def calculate_tokens_spent(lines, offset):
    result = 0

    for line in lines:
        if line.startswith("Button"):
            parts = line.split(" ")
            button_type = parts[1].split(":")[0]

            if button_type == 'A':
                x_move_button_A = int(parts[2][2:-1])
                y_move_button_A = int(parts[3][2:])
            else:
                x_move_button_B = int(parts[2][2:-1])
                y_move_button_B = int(parts[3][2:])
        elif line.startswith("Prize"):
            parts = line.split(" ")
            prize_x = int(parts[1][2:-1]) + offset
            prize_y = int(parts[2][2:]) + offset
            determinant = x_move_button_A * y_move_button_B - y_move_button_A * x_move_button_B

            if determinant != 0:
                a = (prize_x * y_move_button_B - prize_y * x_move_button_B) / determinant
                b = (prize_y * x_move_button_A - prize_x * y_move_button_A) / determinant

                if a == int(a) and b == int(b): result += (3 * a + b) # check for integer solution

    return int(result)

if __name__ == '__main__':
    lines = [line.strip() for line in open('input.txt')]

    print("Part One Solution: " + str(calculate_tokens_spent(lines, 0)))
    print("Part Two Solution: " + str(calculate_tokens_spent(lines, 10_000_000_000_000)))
