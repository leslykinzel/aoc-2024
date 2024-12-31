from typing import Any
import itertools

def eval_left_to_right(expression: list[Any]) -> int:
    '''
        Eval list expression left to right.
    '''
    expression = expression[:]
    ans = expression[0]

    i = 0
    while i < len(expression) - 1:
        match expression[i]:
            case '+':
                ans += expression[i+1]
            case '*':
                ans *= expression[i+1]
            case _:
                pass
        i+=1

    return ans


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

    part1_sum_of_valid_targets = 0
    targets = []
    factors = []

    with open('input.txt', 'r') as file:
        for line in file:
            line = line.strip()

            target, factor = line.split(':')

            # targets contains duplicates!!!
            targets.append(int(target))
            factors.append(list(map(int, factor.split())))

    part1_all_permutations = []
    for f in factors:
        part1_all_permutations.append(get_all_possible_expressions(f, ['+', '*']))

    for i in range(len(targets)):
        exp_list = part1_all_permutations[i] # list of all expressions, matches targets[i]
        target = targets[i]

        for exp in exp_list:
            ans = eval_left_to_right(exp)
            if ans == target:
                print('exp:', exp)
                print('ans:', ans)
                print(f'ans {ans} == target {target}')
                print('======================')
                part1_sum_of_valid_targets += ans
                break # exit so you don't count targets twice.

    print(part1_sum_of_valid_targets)


if __name__ == '__main__':
    main()
