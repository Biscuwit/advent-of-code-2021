from pathlib import Path


with open('input.txt', 'r') as file:
    data = file.readlines()
    nums = [line.rstrip() for line in data]


def day1_A():
    counter = sum(x < y for x, y in zip(nums, nums[1:]))
    print(counter)


def day1_B():
    windows = [int(nums[i]) + int(nums[i+1]) + int(nums[i+2]) for i, _ in enumerate(nums) if i <= 1997]
    counter = sum(x < y for x, y in zip(windows, windows[1:]))
    print(counter)



if __name__ == '__main__':
    day1_A()
    day1_B()
