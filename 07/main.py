from itertools import permutations

def main():

    data = {}

    with open('input.txt', 'r') as file:
        for line in file:
            lr = line.strip().split(':')
            data[int(lr[0].strip())] = list(map(int, lr[1].strip().split()))

    for final_num, factors in data.items():
        required_operators = len(factors)-1

def eval(expression: str):
    pass

if __name__ == '__main__':
    main()