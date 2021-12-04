import copy
import os


def main(input_path: str = ''):
    with open(input_path) as f:
        input_lines = [line for line in f.read().strip().split('\n') if line]
        numbers = [int(x) for x in input_lines.pop(0).split(',')]
        boards = []
        for i in range(0, len(input_lines), 5):
            board = Board([[int(x) for x in input_lines[i+offset].split(' ') if x] for offset in range(5)])
            boards.append(board)
    for i in range(4):
        for b in boards:
            b.mark(numbers[i])
    one(numbers, copy.deepcopy(boards))
    two(numbers, boards)


class Board:
    def __init__(self, data: list):
        self._data = data

    def mark(self, number: int):
        for line in self._data:
            if number in line:
                line[line.index(number)] = -1
                break

    def check(self) -> bool:
        for i in range(5):
            if all([x == -1 for x in self._data[i]]):
                return True
            if all([self._data[line][i] == -1 for line in range(5)]):
                return True
        return False

    def sum_remaining(self) -> int:
        return sum([sum([x if x != -1 else 0 for x in line]) for line in self._data])


def one(numbers: [int], boards: [Board]):
    for i in range(4, len(numbers)):
        for b in boards:
            b.mark(numbers[i])
            if b.check():
                result = b.sum_remaining() * numbers[i]
                print(result)
                return
    return


def two(numbers: [int], boards: [Board]):
    for i in range(4, len(numbers)):
        for b in boards:
            b.mark(numbers[i])
            if b.check():
                if len(boards) > 1:
                    boards.remove(b)
                else:
                    result = b.sum_remaining() * numbers[i]
                    print(result)
                    return
    return


if __name__ == '__main__':
    input_file = './input'
    if os.path.isfile(input_file):
        main(input_file)
    else:
        main()
