import copy
import os
from collections import Counter


def apply_rules(pair_counts: Counter, rules: dict[str, str]):
    next_pair_counts = Counter()
    for c in pair_counts:
        if c in rules:
            next_pair_counts.update({c[0]+rules[c]: pair_counts[c],
                                     rules[c]+c[1]: pair_counts[c]})
        else:
            next_pair_counts.update({c: pair_counts[c]})
    return next_pair_counts


def apply_rules_times(pair_counts, rules, times):
    next_pair_counts = copy.deepcopy(pair_counts)
    for i in range(times):
        next_pair_counts = apply_rules(next_pair_counts, rules)
    element_counts = Counter()
    for c in next_pair_counts:
        element_counts.update({c[0]: next_pair_counts[c]})
        element_counts.update({c[1]: next_pair_counts[c]})
    return element_counts


def main(input_path: str = ''):
    with open(input_path) as f:
        template, _, *rules = f.read().strip().split('\n')
        rules = dict([tuple(line.split(' -> ')) for line in rules])
        pair_counts = Counter([template[i:i+2] for i in range(len(template)-1)])

        element_counts = apply_rules_times(pair_counts, rules, 10)
        element_counts.update([template[0], template[-1]])
        print(max(element_counts.values())//2 - min(element_counts.values())//2)
        element_counts = apply_rules_times(pair_counts, rules, 40)
        element_counts.update([template[0], template[-1]])
        print(max(element_counts.values())//2 - min(element_counts.values())//2)


if __name__ == '__main__':
    input_file = './input'
    if os.path.isfile(input_file):
        main(input_file)
    else:
        main()
