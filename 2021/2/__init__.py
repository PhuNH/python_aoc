def main(input_path: str = ''):
    with open(input_path) as f:
        input_lines = f.readlines()
    
    x, y, depth = 0, 0, 0
    for line in input_lines:
        parts = line.split()
        value = int(parts[1])
        if parts[0] == 'forward':
            x += value
            depth += y * value
        elif parts[0] == 'up':
            y -= value
        else:
            y += value
    print(x*y)
    print(x*depth)
