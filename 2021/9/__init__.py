import os

from libs.vector import Vector, Area


def main(input_path: str = ''):
    with open(input_path) as f:
        area = Area([[int(h) for h in line] for line in f.read().strip().split('\n')])

        def is_higher_than(v: Vector):
            return lambda m: area.at(m) > area.at(v)

        risk_sum = 0
        processing = []
        for y in range(area.height):
            for x in range(area.width):
                current = Vector(x, y)
                if all(map(is_higher_than(current), area.adjacents(current))):
                    risk_sum += 1 + area[y][x]
                    processing.append(Vector(x, y))
        print(risk_sum)

        basin_points = set(processing)
        basin_size = 0
        basin_sizes = []
        while True:
            current = processing.pop()
            adjacents = area.adjacents(current)
            higher = set(filter(is_higher_than(current), adjacents))
            if higher == adjacents:
                if basin_size > 0:
                    basin_sizes.append(basin_size)
                basin_size = 1
            else:
                basin_size += 1
            next_level = list(filter(lambda v: area.at(v) < 9 and v not in basin_points, higher))
            basin_points = basin_points.union(next_level)
            processing.extend(next_level)

            if len(processing) == 0:
                if basin_size > 0:
                    basin_sizes.append(basin_size)
                break
        basin_sizes.sort(reverse=True)
        print(basin_sizes[0] * basin_sizes[1] * basin_sizes[2])


if __name__ == '__main__':
    input_file = './input'
    if os.path.isfile(input_file):
        main(input_file)
    else:
        main()
