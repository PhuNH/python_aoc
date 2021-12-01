import argparse
import importlib
import os

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('year', type=int)
    parser.add_argument('day', type=int)
    args = parser.parse_args()

    module = importlib.import_module(f'{args.year}.{args.day}')
    input_file = f'{args.year}/{args.day}/input'
    if os.path.isfile(input_file):
        module.main(input_file)
    else:
        module.main()
