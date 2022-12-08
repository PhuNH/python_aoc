import os


def main(input_path: str = ''):
    with open(input_path) as f:
        # remove newline characters as they can get in our way
        # keep whitespaces at line beginning as they are usually parts of the input
        # heights = [[int(h) for h in line] for line in f.read().rstrip().splitlines()]
        grid = f.read().rstrip().splitlines()
        count = 2 * len(grid) + 2 * len(grid[0]) - 4
        max_score = 0
        for y in range(1, len(grid) - 1):
            for x in range(1, len(grid[0]) - 1):
                f = lambda o: o < grid[y][x]
                visible = all(map(f, grid[y][:x])) or all(map(f, grid[y][x + 1:])) or \
                    all(map(f, [grid[i][x] for i in range(0, y)])) or \
                    all(map(f, [grid[i][x] for i in range(y+1, len(grid))]))
                if visible:
                    count += 1

                score = 1
                for j in range(x-1, -1, -1):
                    if grid[y][j] >= grid[y][x]:
                        break
                score *= x-1 - j + 1
                for i in range(y-1, -1, -1):
                    if grid[i][x] >= grid[y][x]:
                        break
                score *= y-1 - i + 1
                for j in range(x+1, len(grid[0])):
                    if grid[y][j] >= grid[y][x]:
                        break
                score *= j - (x+1) + 1
                for i in range(y+1, len(grid)):
                    if grid[i][x] >= grid[y][x]:
                        break
                score *= i - (y+1) + 1
                if score > max_score:
                    max_score = score
        print(count, max_score)


def func(e, o):
    return e > o


if __name__ == '__main__':
    input_file = './input'
    if os.path.isfile(input_file):
        main(input_file)
    else:
        main()
