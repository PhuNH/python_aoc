import os
import numpy


def main(input_path: str = ''):
    with open(input_path) as f:
        lines = [line.strip() for line in f.readlines()]
    one(lines)
    two(lines)


def one(lines: list[str]):
    line_arrays = [[1 if c == '1' else -1 for c in line] for line in lines]
    sum_array = numpy.sum(line_arrays, 0)
    gamma, epsilon = 0, 0
    for index, x in enumerate(sum_array[::-1]):
        if x > 0:
            gamma += 2 ** index
        else:
            epsilon += 2 ** index
    print(gamma, epsilon)
    print(gamma * epsilon)


def two(lines: list[str]):
    o2 = rating(1, lines, 0)
    co2 = rating(0, lines, 0)
    print(o2, co2)
    print(o2 * co2)


def rating(criteria: int, strings: list[str], index: int) -> int:
    # criteria: o2 -> 1, co2 -> 0
    count = sum([1 if s[index] == '1' else -1 for s in strings])
    filtered = []
    for s in strings:
        if (count >= 0 and s[index] == str(criteria)) or (count < 0 and s[index] == str(1-criteria)):
            filtered.append(s)
    if len(filtered) == 1:
        print(filtered[0])
        return int(filtered[0], 2)
    else:
        return rating(criteria, filtered, index+1)


if __name__ == '__main__':
    input_file = './input'
    if os.path.isfile(input_file):
        main(input_file)
    else:
        main()
