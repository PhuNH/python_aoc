import os
from libs import vector


def fold(dots, axis, value):
    rest = set()
    if axis == 'x':
        for d in dots:
            rest.add(d if d.x < value else vector.Vector(2*value-d.x, d.y))
    else:
        for d in dots:
            rest.add(d if d.y < value else vector.Vector(d.x, 2*value-d.y))
    return rest


def main(input_path: str = ''):
    with open(input_path) as f:
        parts = f.read().strip().split('\n\n')
        dots = set()
        for line in parts[0].split('\n'):
            xy = map(lambda n: int(n), line.split(','))
            dots.add(vector.Vector(xy.__next__(), xy.__next__()))
        count = 0
        for line in parts[1].split('\n'):
            important = line.rsplit(' ', 1)[1]
            axis_value = important.split('=')
            axis = axis_value[0]
            value = int(axis_value[1])
            dots = fold(dots, axis, value)
            count += 1
            if count == 1:
                print(len(dots))
        max_x, max_y = 0, 0
        for d in dots:
            if d.x > max_x:
                max_x = d.x
            if d.y > max_y:
                max_y = d.y
        for i in range(max_y+1):
            for j in range(max_x+1):
                print('#' if vector.Vector(j, i) in dots else ' ', end='')
            print('\n', end='')


if __name__ == '__main__':
    input_file = './input'
    if os.path.isfile(input_file):
        main(input_file)
    else:
        main()
