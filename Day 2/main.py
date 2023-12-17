if __name__ == "__main__":
    file = open("input.txt")
    lines = file.readlines()

    red_max = [0] * len(lines)
    green_max = [0] * len(lines)
    blue_max = [0] * len(lines)

    sum = 0
    index = 0
    semi_colon_split = []
    draws = []

    for line in lines:
        colon_split = line.split(':')   
        red = 0
        blue = 0
        green = 0
        for i in colon_split:
            if index % 2 == 1:
                semi_colon_split.append(i.split(';'))
            
            index += 1

    for i in semi_colon_split:
        for j in i:
            word = j.split(' ')
            draws.append(word[1:])

    i = 0

    for draw in draws:
        index = 0

        for word in draw:
            if "red" in word:
                if int(draw[index - 1]) > red_max[i]:
                    red_max[i] = int(draw[index - 1])
            elif "blue" in word:
                if int(draw[index - 1]) > blue_max[i]:
                    blue_max[i] = int(draw[index - 1])
            elif "green" in word:
                if int(draw[index - 1]) > green_max[i]:
                    green_max[i] = int(draw[index - 1])

            index += 1

        if '\n' in word:
            i += 1

    for i in range(len(lines)):
        sum += red_max[i] * blue_max[i] * green_max[i]

    print(sum)
