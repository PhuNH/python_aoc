import os

from libs.vector import Vector


def main(input_path: str = ''):
    with open(input_path) as f:
        lines = []
        for line in f.read().strip().split('\n'):
            parts = line.split(' ')
            start = Vector(*[int(s) for s in parts[0].split(',')])
            end = Vector(*[int(s) for s in parts[2].split(',')])
            lines.append(Line(start, end))
        non_diagonals = [line for line in lines if line.is_vertical() or line.is_horizontal()]
    count_overlaps(non_diagonals)
    count_overlaps(lines)


class Line:
    def __init__(self, start: Vector, end: Vector):
        self._start = start
        self._end = end

    def is_horizontal(self) -> bool:
        return self._start.y == self._end.y

    def is_vertical(self) -> bool:
        return self._start.x == self._end.x

    def points(self) -> list[Vector]:
        x_step = 1 if self._start.x < self._end.x else -1
        y_step = 1 if self._start.y < self._end.y else -1

        if self.is_horizontal():
            return [Vector(x, self._start.y) for x in range(self._start.x, self._end.x+x_step, x_step)]
        elif self.is_vertical():
            return [Vector(self._start.x, y) for y in range(self._start.y, self._end.y+y_step, y_step)]
        else:
            xs = [x for x in range(self._start.x, self._end.x+x_step, x_step)]
            ys = [y for y in range(self._start.y, self._end.y+y_step, y_step)]
            return [Vector(*pair) for pair in list(zip(xs, ys))]


def count_overlaps(lines: list[Line]):
    point_counts = {}
    for line in lines:
        for point in line.points():
            if point in point_counts:
                point_counts[point] += 1
            else:
                point_counts[point] = 1
    overlap_count = len([x for x in point_counts.values() if x > 1])
    print(overlap_count)


if __name__ == '__main__':
    input_file = './input'
    if os.path.isfile(input_file):
        main(input_file)
    else:
        main()
