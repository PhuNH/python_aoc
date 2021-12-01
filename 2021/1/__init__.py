def count_increases(depths: list, offset: int) -> int:
    increases = 0
    for index, depth in enumerate(depths):
        if index >= offset and depth > depths[index-offset]:
            increases += 1
    return increases


def main(input_path: str):
    with open(input_path) as f:
        input_lines = [int(line) for line in f.readlines()]

    print(count_increases(input_lines, 1))
    print(count_increases(input_lines, 3))


if __name__ == '__main__':
    main('./input')