import os
from functools import reduce
from operator import mul


version_sum = 0
ops = [sum, lambda l: reduce(mul, l),
       min, max,
       None, lambda l: int(l[0] > l[1]),
       lambda l: int(l[0] < l[1]), lambda l: int(l[0] == l[1])]


def main(input_path: str = ''):
    with open(input_path) as f:
        # (v6, 2021)
        # input_line = 'D2FE28'
        # (v1, t6, l27 [ (v6, 10), (v2, 20) ])
        # input_line = '38006F45291200'
        # (v7, t3, #3 [ (v2, 1), (v4, 2), (v1, 3) ])
        # input_line = 'EE00D40C823060'
        # (v4, (v1, (v5, (v6, val)))) total 16
        # input_line = '8A004A801A8002F478'
        # (v3, #2 [ (v0, l22 [ (v0, 10), (v5, 11) ]), (v1, #2 [ (v0, 12), (v3, 13) ]) ]) total 12
        # input_line = '620080001611562C8802118E34'
        # (v6, l84 [ (v0, l22 [ (v0, 10), (v6, 11) ]), (v4, #2 [ (v7, 12), (v0, 13) ]) ]) total 23
        # input_line = 'C0015000016115A2E0802F182340'
        # () total 31
        # input_line = 'A0016C880162017C3686B18A3D4780'
        input_line = f.read()
        # instead of this which requires f.read().rstrip() to get the correct length
        '''
        bin_len = 4 * len(input_line)
        input_value = int(input_line, 16)
        binary_data = f'{input_value:0>{bin_len}b}'
        '''
        # do this
        binary_data = bin(int(f'1{input_line}', 16))[3:]
        value, leftover = parse(binary_data)
        print(version_sum, value, leftover)


def parse(data: str):
    global version_sum
    version = int(data[:3], 2)
    version_sum += version

    type_id = int(data[3:6], 2)
    data = data[6:]

    if type_id == 4:
        value_str = ''
        while True:
            prefix = data[0]
            value_str += data[1:5]
            data = data[5:]
            if prefix == '0':
                break
        value = int(value_str, 2)
    else:
        sub_values = []
        if data[0] == '0':
            sub_packets_len = int(data[1:16], 2)
            data = data[16:]
            sub_data = data[:sub_packets_len]
            while sub_data:
                v, sub_data = parse(sub_data)
                sub_values.append(v)
            data = data[sub_packets_len:]
        else:
            sub_packets_num = int(data[1:12], 2)
            data = data[12:]
            for _ in range(sub_packets_num):
                v, data = parse(data)
                sub_values.append(v)
        value = ops[type_id](sub_values)
    return value, data


if __name__ == '__main__':
    input_file = './input'
    if os.path.isfile(input_file):
        main(input_file)
    else:
        main()
