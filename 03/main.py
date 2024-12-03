import re

MULT_EXPRESSION = re.compile(r'mul\((\d+),(\d+)\)')

def main():
    with open('input.txt', 'r') as file:
        data = file.read()

    result = []

    for match in MULT_EXPRESSION.finditer(data):
        result.append(int(match.group(1)) * int(match.group(2)))

    print('Part 1:', sum(result))

if __name__ == '__main__':
    main()