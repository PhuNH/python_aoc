import os
from collections import deque

from libs.vector import Area, Vector


class Risks:
    def __init__(self, risk: int, acc_risk: int = -1):
        self.risk = risk
        self.acc_risk = acc_risk


def shortest_path_tree(area: Area):
    start = Vector(0, 0)
    end = Vector(area.width-1, area.height-1)
    q: deque[(Vector, int)] = deque()
    q.append((start, 0))
    while len(q) > 0:
        current_node, current_acc_risk = q.popleft()
        current_node_risks = area.at(current_node)
        if current_node != start and current_acc_risk > current_node_risks.acc_risk:
            continue
        connected_nodes = area.adjacents(current_node)
        for n in connected_nodes:
            next_node_risks = area.at(n)
            next_acc_risk = current_acc_risk + next_node_risks.risk
            if next_node_risks.acc_risk == -1 or next_acc_risk < next_node_risks.acc_risk:
                next_node_risks.acc_risk = next_acc_risk
                q.append((n, next_acc_risk))
    print(area.at(end).acc_risk)


def main(input_path: str = ''):
    with open(input_path) as f:
        inputs = [[int(h) for h in line] for line in f.read().strip().splitlines()]
        area = Area([[Risks(h) for h in line] for line in inputs])
        shortest_path_tree(area)

        for _ in range(4):
            for row in inputs:
                tail = row[-area.width:]
                row.extend((x+1) if x < 9 else 1 for x in tail)
        for _ in range(4):
            for row in inputs[-area.height:]:
                row = [(x+1) if x < 9 else 1 for x in row]
                inputs.append(row)
        area = Area([[Risks(h) for h in line] for line in inputs])
        shortest_path_tree(area)


if __name__ == '__main__':
    input_file = './input'
    if os.path.isfile(input_file):
        main(input_file)
    else:
        main()
