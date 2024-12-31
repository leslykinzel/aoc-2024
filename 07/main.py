from typing import Any
import itertools

def concat_ints(x: int, y: int) -> int:
    return int(str(x) + str(y))

def eval_concat_operator(expression: list[Any]) -> list[Any]:
    ''' 
        Combine args between || operators.
    '''
    final_expression = []

    i = 0
    while i < len(expression):
        if expression[i] == '||':
            l_val = str(final_expression[-1])
            r_val = str(expression[i + 1])
            final_expression[-1] = int(l_val + r_val)

            i+=1 # skip next
        else:
            final_expression.append(expression[i])
        i+=1

    return final_expression

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

    sum_of_valid_targets = 0
    targets = []
    factors = []

    with open('test.txt', 'r') as file:
        for line in file:
            line = line.strip()

            target, factor = line.split(':')

            # targets contains duplicates!!!
            targets.append(int(target))
            factors.append(list(map(int, factor.split())))

    # targets: list[int]
    # factors: list[list[int]]

    all_permutations = []
    for f in factors:
        all_permutations.append(get_all_possible_expressions(f, ['+', '*', '||']))

    # print(all_permutations)
    for i in range(len(targets)):
        exp_list = all_permutations[i] # list of all expressions, matches targets[i]
        target = targets[i]

        for exp in exp_list:
            exp = eval_concat_operator(exp)
            ans = eval_left_to_right(exp)
            if ans == target:
                print('exp:', exp)
                print('ans:', ans)
                print(f'ans {ans} == target {target}')
                print('======================')
                sum_of_valid_targets += ans
                break # exit so you don't count targets twice.


if __name__ == '__main__':
    main()
