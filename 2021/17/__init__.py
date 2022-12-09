import math
import os

from libs.vector import Vector


def v_limit(e, t):
    return (e + t * (t - 1) / 2) / t


def s_t(s_0, t):
    return s_0 * t - t*(t - 1)/2


def main(input_path: str = ''):
    with open(input_path) as f:
        # remove newline characters as they can get in our way
        # keep whitespaces at line beginning as they are usually parts of the input
        input_line = f.read().rstrip().split(':')[1]
        x_interval = input_line.split(',')[0].strip().split('=')[1].split('..')
        X = (int(x_interval[0]), int(x_interval[1]))
        y_interval = input_line.split(',')[1].strip().split('=')[1].split('..')
        Y = (int(y_interval[0]), int(y_interval[1]))

        # part 1
        print(int(Y[0] * (Y[0] + 1) / 2))

        # part 2
        # t <= v_x(0)
        starts = set()
        for ds in range(X[0]-Y[1], X[1]-Y[0]+1):
            for t in range(1, math.floor(ds/2)+1):
                if ds % t == 0:
                    dv = int(ds / t)
                    v_x_limit_left = max(t, math.ceil(v_limit(X[0], t)))
                    v_x_limit_right = math.floor(v_limit(X[1], t))
                    starts |= set([Vector(v_x, v_x - dv) for v_x in range(v_x_limit_left, v_x_limit_right+1)
                                   if Y[0] <= s_t(v_x - dv, t) <= Y[1]])
        # t > v_x(0)
        v_x = 21  # 21 * (21 + 1) / 2 in [217, 240]
        t = v_x + 1
        while True:
            right = v_limit(Y[1], t)
            left = v_limit(Y[0], t)
            if right - left < .001:
                break
            v_y_limit_left = math.ceil(left)
            v_y_limit_right = math.floor(right)
            starts |= set([Vector(v_x, v_y) for v_y in range(v_y_limit_left, v_y_limit_right+1)])
            t += 1
        print(len(starts))


if __name__ == '__main__':
    input_file = './input'
    if os.path.isfile(input_file):
        main(input_file)
    else:
        main()
