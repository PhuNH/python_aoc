# Python AoC
Advent of Code 2021 in Python

### Run
At project root:
```shell
python -m aoc <year> <day>
```
Or at a day's directory:
```shell
python -m __init__
```

### Structure
- Each year is a directory, each day is a package (i.e. a directory containing `__init__.py` file) inside the year directory;
- In each day directory:
  - `__init__.py` file contains code for the day with a `main(input_path: str = '')` function;
  - Possibly an `input` file.

### Others
2015, 2018, 2019, 2020: [Scala](https://github.com/PhuNH/scala_aoc)  
2016, 2017: [Rust](https://github.com/PhuNH/rust_aoc)