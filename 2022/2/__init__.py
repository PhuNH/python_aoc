import os


def main(input_path: str = ''):
    with open(input_path) as f:
        pairs = [line.split(' ') for line in f.read().strip().splitlines()]
        one(pairs)
        two(pairs)


def one(pairs):
    total = 0
    for pair in pairs:
        diff = ord(pair[1]) - ord(pair[0])
        shape_score = ord(pair[1]) - 87
        if diff == 23:
            score = shape_score + 3
        elif diff == 24 or diff == 21:
            score = shape_score + 6
        else:  # diff == 22 or diff == 25
            score = shape_score
        total += score
    print(total)


def two(pairs):
    total = 0
    for pair in pairs:
        if pair[1] == 'Y':
            score = 3 + ord(pair[0]) - 64
        elif pair[1] == 'Z':
            score = 6 + ord(pair[0]) - 64 + (1 if ord(pair[0]) < ord('C') else -2)
        else:
            score = ord(pair[0]) - 64 + (-1 if ord(pair[0]) > ord('A') else 2)
        total += score
    print(total)


if __name__ == '__main__':
    input_file = './input'
    if os.path.isfile(input_file):
        main(input_file)
    else:
        main()
