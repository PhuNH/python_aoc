import os


def main(input_path: str = ''):
    with open(input_path) as f:
        crabs = [int(x) for x in f.read().strip().split(',')]
        crabs.sort()
        median = crabs[len(crabs)//2]
        print(sum([abs(x-median) for x in crabs]))

        # got this from reddit
        mean = sum(crabs) // len(crabs)
        print(sum([sequence_sum(abs(x-mean)) for x in crabs]))

        # import sys
        # least_fuels = sys.maxsize
        # for i in range(crabs[0], crabs[-1]+1):
        #     fuels = sum([sequence_sum(abs(x-i)) for x in crabs])
        #     if least_fuels > fuels:
        #         least_fuels = fuels
        # print(least_fuels)


def sequence_sum(x):
    return x * (x+1) // 2


if __name__ == '__main__':
    input_file = './input'
    if os.path.isfile(input_file):
        main(input_file)
    else:
        main()
