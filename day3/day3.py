import numpy as np
with open('input.txt', 'r') as file:
    data = file.readlines()
    codes = [line.rstrip() for line in data]
split_codes = []
for code in codes:
    split = [int(val) for val in code]
    split_codes.append(split)
trans = np.transpose(split_codes)


def day3_A():
    gamma_str = ''
    epsilon_str = ''
    for row in trans:
        gamma_str += str(find_bit(row, True))
        epsilon_str += str(find_bit(row, False))
    gamma = int(gamma_str, 2)
    epsilon = int(epsilon_str, 2)
    print(f'{gamma_str}: {gamma}')
    print(f'{epsilon_str}: {epsilon}')
    ans = gamma * epsilon
    print(ans)


def day3_B():
    oxygen_codes = split_codes.copy()
    co2_codes = split_codes.copy()
    oxygen_rating = find_rating(oxygen_codes, True, 'o')
    co2_rating = find_rating(co2_codes, False, 'c')
    print(oxygen_rating * co2_rating)

def find_rating(codes, most, rating):
    bit_loc = 0
    while len(codes)-1:
        flipped_codes = np.transpose(codes)
        common_bit = find_bit(flipped_codes[bit_loc], most, rating)
        rows_to_delete = [o_code for o_code in codes if common_bit != o_code[bit_loc]]
        for row in rows_to_delete:
            codes.remove(row)
        bit_loc += 1
    s = [str(x) for x in codes[0]]
    return int(''.join(s), 2)


def find_bit(row, most, rating=''):
    count = np.bincount(row)
    if count[0] == count[1] and rating:
        if rating == 'o':
            return 1
        else:
            return 0
    if most:
        return count.argmax()
    else:
        return count.argmin()


if __name__ == '__main__':
    day3_A()
    day3_B()