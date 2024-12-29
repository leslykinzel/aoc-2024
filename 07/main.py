import itertools

def concat_ints(x: int, y: int) -> int:
    return int(str(x) + str(y))

def left_to_right_eval(factors: list[int], operators: list[str]) -> int:
    ''' 
        This challenge is so stupid...
    '''
    if len(factors) - 1 != len(operators):
        raise Exception(f"What happened here?\n{factors}\n{operators}")

    i = 0
    while i < len(operators):
        if operators[i] == '||':
            factors[i] = concat_ints(factors[i], factors[i + 1])
            del factors[i + 1]
            del operators[i]
        else: 
            i += 1

    result = factors[0]

    for i in range(len(operators)):
        match operators[i]:
            case '+':
                result += factors[i + 1]
            case '*':
                result *= factors[i + 1]

    return result


def factors_can_make_target(factors: list, target:int) -> bool:
    '''
        If any permutation of operators can equal the target when 
        evaluated left-to-right (ignoring operator precedence), 
        return True.
    '''
    operators = [ '+', '*', '||' ]
    total_ops = len(factors) - 1
    op_combos = list(itertools.product(operators, repeat=total_ops))

    for ops in op_combos:
        copyof_factors = factors.copy()
        if left_to_right_eval(copyof_factors, list(ops)) == target:
            return True

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

    for i in range(len(targets)):
        if factors_can_make_target(factors[i], targets[i]):
            sum_of_valid_targets += targets[i]
        else:
            continue

    print('Part 1:', sum_of_valid_targets)


if __name__ == '__main__':
    main()