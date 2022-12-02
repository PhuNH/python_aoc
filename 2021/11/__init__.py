import os

from libs.vector import Area, Vector


def main(input_path: str = ''):
    with open(input_path) as f:
        area = Area([[int(o) for o in line] for line in f.read().strip().split('\n')])
        total_flashes = 0
        step = 1
        while True:
            flashes, s = update(area)
            total_flashes += flashes
            if step == 100:
                print(total_flashes)
            if s:
                print(step)
                break
            step += 1


def get_new_flashes(area: Area, flashes: set) -> set:
    new_flashes = set()
    for y in range(area.height):
        for x in range(area.width):
            current = Vector(x, y)
            if current not in flashes and area[y][x] >= 9:
                new_flashes.add(current)
    return new_flashes


def update(area: Area) -> (int, bool):
    flashes = set()
    new_flashes = get_new_flashes(area, flashes)
    while len(new_flashes) > 0:
        for f in new_flashes:
            for neigh in area.diag_adjacents(f):
                area.set_at(neigh, area.at(neigh) + 1)
            flashes.add(f)
        new_flashes = get_new_flashes(area, flashes)
    for y in range(area.height):
        for x in range(area.width):
            area[y][x] = 0 if Vector(x, y) in flashes else area[y][x] + 1
    flash_count = len(flashes)
    return flash_count, flash_count == area.width * area.height


if __name__ == '__main__':
    input_file = './input'
    if os.path.isfile(input_file):
        main(input_file)
    else:
        main()
