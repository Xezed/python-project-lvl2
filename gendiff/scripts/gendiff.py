import argparse
import json


def main():
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', help='set format of output')
    args = parser.parse_args()

    if args.first_file and args.second_file:
        generate_diff(args.first_file, args.second_file)


def generate_diff(path_one, path_two):
    first_file = json.load(open(path_one))
    second_file = json.load(open(path_two))

    result = '{\n'
    for key in sorted({*first_file, *second_file}):
        first_file_val = first_file.get(key)
        second_file_val = second_file.get(key)
        if first_file_val == second_file_val:
            result += f'    {key}: {first_file_val}\n'
        elif first_file_val != second_file_val:
            if first_file_val and second_file_val:
                result += f'    - {key}: {first_file_val}\n'
                result += f'    + {key}: {second_file_val}\n'
            elif first_file_val and not second_file_val:
                result += f'    - {key}: {first_file_val}\n'
            else:
                result += f'    + {key}: {first_file_val}\n'

    result += '}'
    print(result)


if __name__ == '__main__':
    main()
