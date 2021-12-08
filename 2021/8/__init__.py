import os

easy_digit_segment_counts = {2: 1, 4: 4, 3: 7, 7: 8}


def main(input_path: str = ''):
    with open(input_path) as f:
        lines = f.read().strip().split('\n')
        easy_output_count = 0
        total = 0
        for line in lines:
            parts = [x.strip() for x in line.split('|')]
            input_parts, output_parts = [set(p) for p in parts[0].split()], [set(p) for p in parts[1].split()]
            output_sum = 0
            digits = find_digits(input_parts)

            for index, s in enumerate(output_parts):
                if len(s) in easy_digit_segment_counts:
                    easy_output_count += 1
                factor = 10**(3-index)
                for num, d in enumerate(digits):
                    if d == s:
                        output_sum += factor * num
                        break
            # print(output_sum)
            total += output_sum
        print(easy_output_count)
        print(total)


def find_digits(input_parts: list) -> list:
    digits = [set()] * 10
    segments = [''] * 7
    group_069, group_235 = [], []
    for p in input_parts:
        if len(p) in easy_digit_segment_counts:
            digits[easy_digit_segment_counts[len(p)]] = p
        elif len(p) == 6:
            group_069.append(p)
        else:
            group_235.append(p)
    segments[0] = digits[7].difference(digits[1]).pop()
    union_1_3 = digits[4].difference(digits[1])
    union_0_1_5_6 = group_069[0].intersection(group_069[1]).intersection(group_069[2])
    segments[3] = union_1_3.union(segments[0]).difference(union_0_1_5_6).pop()
    segments[1] = union_1_3.difference(segments[3]).pop()
    digits[0] = next(filter(lambda s: segments[3] not in s, group_069))
    union_4_6 = digits[0].difference(digits[1]).difference(segments[0], segments[1])
    segments[4] = union_4_6.difference(union_0_1_5_6).pop()
    digits[9] = next(filter(lambda s: segments[4] not in s, group_069))
    digits[6] = next(filter(lambda s: s != digits[0] and s != digits[9], group_069))
    digits[3] = digits[9].difference(segments[1])
    digits[5] = digits[6].difference(segments[4])
    digits[2] = next(filter(lambda s: s != digits[3] and s != digits[5], group_235))
    return digits


if __name__ == '__main__':
    input_file = 'input'
    if os.path.isfile(input_file):
        main(input_file)
    else:
        main()
