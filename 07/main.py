import itertools

def concat_ints(x: int, y: int) -> int:
    return int(str(x) + str(y))

def left_to_right_eval(factors: list[int], operators: list[str]) -> int:
    ''' 
        This challenge is so stupid...
    '''
    result = factors[0]

    for i in range(len(operators)):
        match operators[i]:
            case '+':
                result += factors[i + 1]
            case '*':
                result *= factors[i + 1]

    return result


def factors_can_make_target(expressions: list) -> bool:
    '''
        If any permutation of operators can equal the target when 
        evaluated left-to-right (ignoring operator precedence), 
        return True.
    '''
    return False

def main():

    targets = []
    factors = []

    with open('test.txt', 'r') as file:
        for line in file:
            line = line.strip()

            target, factor = line.split(':')

            targets.append(int(target))
            factors.append(list(map(int, factor.split())))

    sum_of_valid_targets = 0
    test_ops = [ '*', '+', '*' ]
    test_num = [ 1, 2, 3, 4]

    merged = [item for pair in itertools.zip_longest(test_num, test_ops, fillvalue=None) for item in pair]
    merged.remove(None)
    print(merged)

    print('ANS:', sum_of_valid_targets)


if __name__ == '__main__':
    main()