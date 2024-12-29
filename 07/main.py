import itertools

def concat_ints(x: int, y: int) -> int:
    return int(str(x) + str(y))

def left_to_right_eval(factors: list[int], operators: list[str]) -> int:
    ''' 
        This challenge is so stupid...
    '''
    result = factors[0]

    i = 0

    while i < len(operators):
        if i + 1 < len(factors):
            match operators[i]:
                case '+':
                    result += factors[i + 1]
                case '*':
                    result *= factors[i + 1]
                case '||':
                    factors[i] = concat_ints(factors[i], factors[i + 1])

            i += 1

    return result


def factors_can_make_target(factors: list, target:int) -> bool:
    '''
        If any permutation of operators can equal the target when 
        evaluated left-to-right (ignoring operator precedence), 
        return True.
    '''
    operators = [ '+', '*' ]
    total_ops = len(factors) - 1
    op_combos = list(itertools.product(operators, repeat=total_ops))

    for ops in op_combos:
        if left_to_right_eval(factors, list(ops)) == target:
            return True

    return False


def main():

    targets = []
    factors = []

    with open('input.txt', 'r') as file:
        for line in file:
            line = line.strip()

            target, factor = line.split(':')

            targets.append(int(target))
            factors.append(list(map(int, factor.split())))

    sum_of_valid_targets = 0

    for i in range(len(targets)):
        if factors_can_make_target(factors[i], targets[i]):
            sum_of_valid_targets += targets[i]
        else:
            continue

    print('Part 1:', sum_of_valid_targets)


if __name__ == '__main__':
    main()