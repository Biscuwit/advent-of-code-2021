from pathlib import Path


with open('input.txt', 'r') as file:
    data = file.readlines()
    instructions = [line.rstrip() for line in data]


def day2_A():
    x, y = 0, 0
    instructions_dict = {'down': [], 'up': [], 'forward': []}
    for line in instructions:
        temp = line.split(' ')
        instruction = temp[0]
        val = int(temp[1])
        instructions_dict[instruction].append(val)
    x = sum(instructions_dict['forward'])
    y = sum(instructions_dict['down']) - sum(instructions_dict['up'])
    print(x, y, x*y)


def day2_B():
    x, y, aim = 0, 0, 0

    for line in instructions:
        temp = line.split(' ')
        if temp[0] == 'forward':
            y += int(temp[1])*aim
            x += int(temp[1])
        elif temp[0] == 'down':
            aim += int(temp[1])

        elif temp[0] == 'up':
            aim -= int(temp[1])
        print(x, y, aim)

    print(x, y, x*y)



if __name__ == '__main__':
    day2_A()
    day2_B()
