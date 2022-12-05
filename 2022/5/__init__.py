import copy
import os


def main(input_path: str = ''):
    with open(input_path) as f:
        inputs = f.read().split('\n\n')
        initial = inputs[0]
        procedure = inputs[1]

        initial_lines = initial.splitlines()
        n = len(initial_lines[-1].strip().split())
        o_stacks = [[] for _ in range(n)]
        for line in initial_lines[-2::-1]:
            for i in range(n):
                if (c := line[1+4*i]) != ' ':
                    o_stacks[i].append(c)

        first_stacks = copy.deepcopy(o_stacks)
        second_stacks = copy.deepcopy(o_stacks)
        for line in procedure.splitlines():
            words = line.split(' ')
            count, src, dst = int(words[1]), int(words[3]) - 1, int(words[5]) - 1

            first_stacks[dst].extend(first_stacks[src][-1:-count-1:-1])
            first_stacks[src] = first_stacks[src][:-count]
            second_stacks[dst].extend(second_stacks[src][-count:])
            second_stacks[src] = second_stacks[src][:-count]
        print(''.join([s[-1] for s in first_stacks]))
        print(''.join([s[-1] for s in second_stacks]))


if __name__ == '__main__':
    input_file = './input'
    if os.path.isfile(input_file):
        main(input_file)
    else:
        main()
