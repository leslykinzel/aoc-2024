import pandas as pd
from collections import Counter

def main():
    ''' Part 1 - Compare distance '''
    df = pd.read_csv('input.txt', sep=r'\s+', header=None, engine='python')

    col_1 = sorted(df[0])
    col_2 = sorted(df[1])

    result = [abs(x - y) for x, y in zip(col_1, col_2)]

    print('Part 1:', sum(result))

    ''' Part 2 - Similarity score '''
    counts = Counter(col_2)
    result = [col_1[i] * counts[col_1[i]] for i in range(len(col_1))]

    print('Part 2:', sum(result))

if __name__ == '__main__':
    main()
