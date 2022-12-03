import os


def main(input_path: str = ''):
    with open(input_path) as f:
        error_priority_sum = 0
        badge_priority_sum = 0
        group = []
        for index, line in enumerate(f.read().strip().splitlines()):
            error_priority_sum += priority(error(line))
            group.append(set(line))
            if index % 3 == 2:
                badge_priority_sum += priority((group[0] & group[1] & group[2]).pop())
                group = []
        print(error_priority_sum, badge_priority_sum)


def priority(e: str) -> int:
    if e.islower():
        return ord(e) - 96  # 97 to 122
    else:
        return ord(e) - 38  # 65 to 90


def error(line: str) -> str:
    rucksack_size = int(len(line) / 2)
    first, second = set(line[:rucksack_size]), set(line[rucksack_size:])
    return (first & second).pop()


if __name__ == '__main__':
    input_file = './input'
    if os.path.isfile(input_file):
        main(input_file)
    else:
        main()
