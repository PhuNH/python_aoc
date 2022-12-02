import os
from collections import deque

from libs.path import Path


class TwicePath(Path):
    def __init__(self, start):
        super().__init__(start)
        self.twice = False

    def add_second(self):
        self.twice = True


def main(input_path: str = ''):
    with open(input_path) as f:
        connections = {}
        for line in f.read().strip().split('\n'):
            names = line.split('-')
            for i, name in enumerate(names):
                if name not in connections:
                    connections[name] = set()
                connections[name].add(names[1-i])
    one(connections)
    two(connections)


def one(connections: dict[str, set[str]]):
    count = 0
    q: deque[Path] = deque()
    q.append(Path('start'))
    while len(q) > 0:
        current_path = q.popleft()
        current_node = current_path.nodes[-1]
        connected_nodes = connections[current_node]
        for n in connected_nodes:
            if n == 'end':
                count += 1
            elif n.islower():
                if n not in current_path:
                    q.append(current_path.add_node(n))
            else:
                q.append(current_path.add_node(n))
    print(count)


def two(connections: dict[str, set[str]]):
    count = 0
    q: deque[TwicePath] = deque()
    q.append(TwicePath('start'))
    while len(q) > 0:
        current_path = q.popleft()
        current_node = current_path.nodes[-1]
        connected_nodes = connections[current_node]
        for n in connected_nodes:
            if n == 'end':
                count += 1
            elif n == 'start':
                continue
            elif n.islower():
                if n not in current_path:
                    q.append(current_path.add_node(n))
                elif not current_path.twice:
                    next_path = current_path.add_node(n)
                    next_path.add_second()
                    q.append(next_path)
            else:
                q.append(current_path.add_node(n))
    print(count)


if __name__ == '__main__':
    input_file = './input'
    if os.path.isfile(input_file):
        main(input_file)
    else:
        main()
