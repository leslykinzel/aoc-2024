import pandas as pd

def main():
    df = pd.read_csv('input.txt', sep=r'\s+', header=None, engine='python')

    col_1 = sorted(df[0])
    col_2 = sorted(df[1])

    result = [abs(c1 - c2) for c1, c2 in zip(col_1, col_2)]

    print(sum(result))

if __name__ == '__main__':
    main()