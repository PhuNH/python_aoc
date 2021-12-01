def count_increases(depths: list, offset: int) -> int:
    increases = 0
    for index, depth in enumerate(depths):
        if index >= offset and depth > depths[index-offset]:
            increases += 1
    return increases


with open('input') as f:
    input_lines = [int(line) for line in f.readlines()]

print(count_increases(input_lines, 1))
print(count_increases(input_lines, 3))
