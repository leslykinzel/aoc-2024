import re

def main():
    matches = re.findall(r'mul\(\d+,\d+\)|do\(\)|don\'t\(\)', open('input.txt', 'r').read())

    p1_result = ''
    p2_result = ''

    do = True
    for match in matches:
        if match == 'do()':
            do = True
        elif match == 'don\'t()':
            do = False

        ''' Part 1 - Find all Mult Expressions '''
        if match.startswith('mul'):
            p1_result += match

        ''' Part 2 - Only process after do() '''
        if do and match.startswith('mul'):
            p2_result += match

    print('Part 1:', sum(match_and_mult(str(p1_result))))
    print('Part 2:', sum(match_and_mult(str(p2_result))))


def match_and_mult(s: str) -> list:
    mult_re = re.compile(r'mul\((\d+),(\d+)\)')
    result = []

    for match in mult_re.finditer(s):
        result.append(int(match.group(1)) * int(match.group(2)))

    return result

if __name__ == '__main__':
    main()