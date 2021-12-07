with open('input.txt', 'r') as file:
    data = list(map(int, file.readline().split(',')))
    max_pos = max(list(data))
    positions = {i: 0 for i in list(range(0, max_pos))}


def day7_a():
    for crab in data:
        for i in range(max_pos):
            positions[i] += abs(crab-i)

    print(min(positions.values()))


def day7_b():
    for crab in data:
        for i in range(max_pos):
            positions[i] += sum(range(abs(crab-i)))

    print(min(positions.values()))


if __name__ == '__main__':
    day7_a()
    day7_b()
