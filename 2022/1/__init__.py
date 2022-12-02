import os


def main(input_path: str = ''):
    with open(input_path) as f:
        sums = [0, 0, 0]
        for line_group in f.read().strip().split('\n\n'):
            group_sum = 0
            for line in line_group.splitlines():
                group_sum += int(line)
            if min(sums) < group_sum:
                sums.remove(min(sums))
                sums.append(group_sum)
        print(max(sums))
        print(sum(sums))


if __name__ == '__main__':
    input_file = './input'
    if os.path.isfile(input_file):
        main(input_file)
    else:
        main()
