import itertools


def factors_can_make_target(factors: list, target:int) -> bool:
    operators = [ '+', '*' ]
    total_ops = len(factors) - 1
    op_combos = list(itertools.product(operators, repeat=total_ops))

    for combo in op_combos:
        expression_parts = [str(factors[0])]

        for i in range(total_ops):
            expression_parts.append(combo[i])
            expression_parts.append(str(factors[i + 1]))

        expression = ''.join(expression_parts)
        if eval(expression) == target:
            print(f'SUCCESS: {expression} == {target}')
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

    print(targets)
    print(factors)
    yes = 0

    for i in range(len(targets)):
        if factors_can_make_target(factors[i], targets[i]):
            yes += 1
        else:
            continue

    print(yes)

if __name__ == '__main__':
    main()