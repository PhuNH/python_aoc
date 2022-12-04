import os
import time

from libs.path import dijkstra_shortest_path_tree, my_shortest_path_tree
from libs.vector import Vector


def main(input_path: str = ''):
    with open(input_path) as f:
        inputs = [[int(h) for h in line] for line in f.read().strip().splitlines()]
        start = Vector(0, 0)
        t0 = time.perf_counter()
        # area = my_shortest_path_tree(inputs, start)
        area = dijkstra_shortest_path_tree(inputs, start)
        print(f'first part: {time.perf_counter() - t0}')
        end = Vector(area.width-1, area.height-1)
        print(area.at(end).tentative)

        for _ in range(4):
            for row in inputs:
                tail = row[-area.width:]
                row.extend((x+1) if x < 9 else 1 for x in tail)
        for _ in range(4):
            for row in inputs[-area.height:]:
                row = [(x+1) if x < 9 else 1 for x in row]
                inputs.append(row)
        t0 = time.perf_counter()
        # area = my_shortest_path_tree(inputs, start)
        area = dijkstra_shortest_path_tree(inputs, start)
        print(f'second part: {time.perf_counter() - t0}')
        end = Vector(area.width-1, area.height-1)
        print(area.at(end).tentative)


if __name__ == '__main__':
    input_file = './input'
    if os.path.isfile(input_file):
        main(input_file)
    else:
        main()
