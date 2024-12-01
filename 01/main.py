import pandas as pd

def main():
    ''' Part 1 - Compare distance '''
    df = pd.read_csv('input.txt', sep=r'\s+', header=None, engine='python')

    col_1 = sorted(df[0])
    col_2 = sorted(df[1])

    result = [abs(x - y) for x, y in zip(col_1, col_2)]

    print('Part 1:', sum(result))

    ''' Part 2 - Similarity score '''
    result = []
    for i in range(len(col_1)):
        mult = col_2.count(col_1[i])
        result.append(col_1[i] * mult)

    print('Part 2:', sum(result))

if __name__ == '__main__':
    main()