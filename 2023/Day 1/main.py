if __name__ == "__main__":
    file = open("input.txt")
    lines = file.readlines()

    left = [None] * len(lines)
    right = [None] * len(lines)
    index = 0

    numbers = {
        "zero": '0',
        "one": '1',
        "two": '2',
        "three": '3',
        "four": '4',
        "five": '5',
        "six": '6',
        "seven": '7',
        "eight": '8',
        "nine": '9'
    }

    line_number = 0

    for line in lines:
        for c in line:
            for x in numbers:
                if (c.isdigit()):
                    if left[line_number] is None:
                        left[line_number] = c
                    
                    right[line_number] = c

                if index < len(line):                 
                    if x == line[index : index + 5] or x == line[index : index + 4] or x == line[index : index + 3]:
                        if left[line_number] is None:
                            left[line_number] = numbers[x]
                        
                        right[line_number] = numbers[x]
                
            index += 1
        
        line_number += 1
        index = 0
    
    values = [None] * len(left)

    for i in range(len(values)):
        values[i] = left[i] + right[i]

    sum = 0

    for i in values:
        sum += int(i)

    print(sum)
