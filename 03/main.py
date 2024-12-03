import re

MULT_EXPRESSION = re.compile(r'mul\((\d+),(\d+)\)')

def main():
    result = []
    with open('input.txt', 'r') as file:
        data = file.read()

    search = MULT_EXPRESSION.finditer(data)
    for match in search:
        result.append(int(match.group(1)) * int(match.group(2)))

    print('Part 1:', sum(result))

if __name__ == '__main__':
    main()