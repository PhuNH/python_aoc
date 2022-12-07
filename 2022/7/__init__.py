from __future__ import annotations

import os
from collections import deque


class File:
    def __init__(self, name, size: int = 0):
        self.name = name
        self.size = size


class Folder(File):
    def __init__(self, name, parent: Folder = None, subfolders: dict[str, Folder] = None,
                 files: dict[str, File] = None):
        super().__init__(name, -1)
        self.parent = parent
        self.subfolders = subfolders if subfolders else {}
        self.files = files if files else {}

    def eval_size_rec(self):
        if self.size == -1:
            file_sum = sum([f.size for f in self.files.values()])
            folder_sum = sum([f.eval_size_rec() for f in self.subfolders.values()])
            self.size = file_sum + folder_sum
        return self.size

    def sum_sizes(self):
        children_sum = sum([f.sum_sizes() for f in self.subfolders.values()])
        return children_sum + (self.size if self.size <= 100000 else 0)

    def find_smallest_not_smaller_than(self, value):
        q = deque([self])
        result = self.size
        while q:
            f = q.popleft()
            if value <= f.size:
                q.extend(f.subfolders.values())
                if f.size < result:
                    result = f.size
        return result


def main(input_path: str = ''):
    root, cd = Folder('/'), None
    with open(input_path) as f:
        # remove newline characters as they can get in our way
        # keep whitespaces at line beginning as they are usually parts of the input
        for command_output in f.read().rstrip().split('$ ')[1:]:
            command, *output = command_output.splitlines()
            if command == 'ls':
                for line in output:
                    parts = line.split(' ')
                    if parts[0] == 'dir':
                        if parts[1] not in cd.subfolders:
                            cd.subfolders[parts[1]] = Folder(parts[1], parent=cd)
                    else:
                        if parts[1] not in cd.files:
                            cd.files[parts[1]] = File(parts[1], int(parts[0]))
            else:
                target = command.split(' ')[1]
                if target == '/':
                    cd = root
                elif target == '..':
                    cd = cd.parent
                else:
                    if target not in cd.subfolders:
                        cd.subfolders[target] = Folder(target, parent=cd)
                    cd = cd.subfolders[target]
    root_size = root.eval_size_rec()
    print(root.sum_sizes())

    total = 70000000
    required_space = 30000000
    least_to_free = required_space - (total - root_size)
    print(root.find_smallest_not_smaller_than(least_to_free))


if __name__ == '__main__':
    input_file = './input'
    if os.path.isfile(input_file):
        main(input_file)
    else:
        main()
