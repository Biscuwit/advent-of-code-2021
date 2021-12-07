from collections import Counter
class Fish():
    def __init__(self, timer):
        self.timer = timer

    def reset_timer(self):
        self.timer = 6

    def reduce_timer(self):
        if not self.timer:
            self.reset_timer()
        else:
            self.timer -= 1

with open('input.txt', 'r') as file:
    lines = file.readlines()[0]
    data = [int(timer) for timer in lines.rstrip().split(',')]


def day6_a():
    # Really slow solution!
    fishes = [Fish(timer) for timer in data]
    for i in range(0, 80):
        new_fishes= []
        for fish in fishes:
            if not fish.timer:
                new_fishes.append(Fish(8))
            fish.reduce_timer()
        fishes.extend(new_fishes)
    print(len(fishes))

def day6_b():
    # representing number of fish with specific timer value as list

    fish_timers = Counter(data)
    for day in range(256):
        print(fish_timers)
        number_of_new_fishes = fish_timers[0]
        for timer in range(8):
            fish_timers[timer] = fish_timers[timer + 1]
        fish_timers[8] = number_of_new_fishes
        fish_timers[6] += number_of_new_fishes

    print(sum(fish_timers.values()))

if __name__ == '__main__':
    day6_a()
    day6_b()
