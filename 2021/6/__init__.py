import os

from collections import Counter


def main(input_path: str = ''):
    with open(input_path) as f:
        fishes = [int(x) for x in f.readline().strip().split(',')]
        counts_by_day = Counter(fishes)
        do_n_days(counts_by_day, 80)
        do_n_days(counts_by_day, 256)


def do_one_day(counts_by_day: {}) -> {}:
    new_counts = {}
    for day in counts_by_day.keys():
        if day == 0:
            new_counts[6] = new_counts.setdefault(6, 0) + counts_by_day[0]
            new_counts[8] = counts_by_day[0]
        else:
            new_counts[day-1] = new_counts.setdefault(day-1, 0) + counts_by_day[day]
    return new_counts


def do_n_days(counts_by_day: {}, n: int):
    for _ in range(n):
        counts_by_day = do_one_day(counts_by_day)
    total = sum(counts_by_day.values())
    print(total)


if __name__ == '__main__':
    input_file = './input'
    if os.path.isfile(input_file):
        main(input_file)
    else:
        main()
