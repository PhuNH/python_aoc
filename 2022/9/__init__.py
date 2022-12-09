import os

from libs.vector import Vector


def main(input_path: str = ''):
    with open(input_path) as f:
        h, t = Vector(0, 0), Vector(0, 0)
        set_t = {t}
        # part 2
        rope = [h]
        rope.extend([Vector(0, 0) for _ in range(9)])
        set_r = {t}
        # remove newline characters as they can get in our way
        # keep whitespaces at line beginning as they are usually parts of the input
        for line in f.read().rstrip().splitlines():
            d, n = line.split(' ')
            for _ in range(int(n)):
                h = h.up if d == 'U' else h.right if d == 'R' else h.down if d == 'D' else h.left
                t = m_t(h, t, set_t)
                # part 2
                rope[0] = h
                for i in range(1, 10):
                    rope[i] = m_t(rope[i-1], rope[i], s=None if i < 9 else set_r)
        print(len(set_t), len(set_r))


def m_t(h, t, s):
    if h in t.diag_adjacents or h == t:
        return t
    if h.x == t.x:
        next_t = t.down if h.y > t.y else t.up
    elif h.y == t.y:
        next_t = t.right if h.x > t.x else t.left
    elif h.y > t.y:
        next_t = t.down_right if h.x > t.x else t.down_left
    else:  # h.y < t.y
        next_t = t.up_right if h.x > t.x else t.up_left
    if s:
        s.add(next_t)
    return next_t


if __name__ == '__main__':
    input_file = './input'
    if os.path.isfile(input_file):
        main(input_file)
    else:
        main()
