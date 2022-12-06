import os


def main(input_path: str = ''):
    with open(input_path) as f:
        input_line = f.read()
        for i in range(3, len(input_line)):
            if len(set(input_line[i-3:i+1])) == 4:
                print(i+1)
                break
        for i in range(13, len(input_line)):
            if len(set(input_line[i-13:i+1])) == 14:
                print(i+1)
                break


if __name__ == '__main__':
    input_file = './input'
    if os.path.isfile(input_file):
        main(input_file)
    else:
        main()
