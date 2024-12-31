from typing import Any
import itertools

def concat_ints(x: int, y: int) -> int:
    return int(str(x) + str(y))

def left_to_right_eval(expression: list[Any]) -> int:
    ''' 
        This challenge is so stupid...
    '''
    result = expression[0]

    for i in range(1, len(expression), 2):
        opr = expression[i]
        num = expression[i + 1]

        match opr:
            case '+':
                result += num
            case '*':
                result *= num

    return result


def get_all_possible_expressions(factors: list[int], operators: list[str]) -> list[list[Any]]:
    ''' 
        Returns all possible expressions with a list of 
        operators for a single list of factors as ints.
    '''
    required_operators = len(factors) - 1
    possible_combos = list(itertools.product(operators, repeat=required_operators))

    # return list of expressions [[ 1, '+', 2, '*', 3 ], [etc], [etc]]
    possible_expressions = []
    for combo in possible_combos:
        # merge each set of operators into list of ints
        expr = (list(itertools.chain(*itertools.zip_longest(factors, list(combo), fillvalue=None))))
        expr_rm_none = [ x for x in expr if x is not None ]
        possible_expressions.append(expr_rm_none)

    return possible_expressions


def main():

    ans = 0
    targets = []
    factors = []

    with open('test.txt', 'r') as file:
        for line in file:
            line = line.strip()

            target, factor = line.split(':')

            targets.append(int(target))
            factors.append(list(map(int, factor.split())))

    # targets: list[int]
    # factors: list[list[int]]
    print(targets)
    print(factors)

    part_1_ops = [ '+', '*' ]
    part_2_ops = [ '+', '*', '||' ]


if __name__ == '__main__':
    main()
