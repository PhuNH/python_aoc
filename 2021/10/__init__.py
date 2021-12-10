import os

pairs = {'(': ')', '[': ']', '{': '}', '<': '>'}
e_scores = {')': 3, ']': 57, '}': 1197, '>': 25137}
c_scores = {'(': 1, '[': 2, '{': 3, '<': 4}


def main(input_path: str = ''):
    e_score_sum = 0
    line_c_scores = []
    with open(input_path) as f:
        for line in f.read().strip().split('\n'):
            kind, score = get_score(line)
            if kind == 0:
                e_score_sum += score
            else:
                line_c_scores.append(score)
        print(e_score_sum)
        line_c_scores.sort()
        print(line_c_scores[len(line_c_scores)//2])


def get_score(line: str) -> (int, int):
    stack = []
    for c in line:
        if c in pairs:
            stack.append(c)
        else:
            if c != pairs[stack.pop()]:
                return 0, e_scores[c]

    c_score = 0
    while len(stack) > 0:
        c_score = c_score * 5 + c_scores[stack.pop()]
    return 1, c_score


if __name__ == '__main__':
    input_file = './input'
    if os.path.isfile(input_file):
        main(input_file)
    else:
        main()
