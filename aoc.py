import argparse
import importlib

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('year', type=int)
    parser.add_argument('day', type=int)
    args = parser.parse_args()

    module = importlib.import_module(f'{args.year}.{args.day}')
    module.main(f'{args.year}/{args.day}/input')
