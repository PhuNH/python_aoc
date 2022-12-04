import os


def main(input_path: str = ''):
    with open(input_path) as f:
        containing_count, overlapping_count = 0, 0
        for line in f.read().strip().splitlines():
            pair = [[int(s) for s in sections.split('-')] for sections in line.split(',')]
            if (pair[0][0] <= pair[1][0] and pair[0][1] >= pair[1][1]) or \
                    (pair[1][0] <= pair[0][0] and pair[1][1] >= pair[0][1]):
                containing_count += 1
            if (pair[0][0] <= pair[1][0] <= pair[0][1]) or (pair[1][0] <= pair[0][0] <= pair[1][1]):
                overlapping_count += 1
        print(containing_count, overlapping_count)


if __name__ == '__main__':
    input_file = './input'
    if os.path.isfile(input_file):
        main(input_file)
    else:
        main()
