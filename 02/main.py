import pandas as pd

def main():
    with open('input.txt', 'r') as file:
        data = [line.split() for line in file.readlines()]

    longest_line = max(len(row) for row in data)

    for i in range(len(data)):
        while len(data[i]) < longest_line:
            data[i].append(None)

    df = pd.DataFrame(data)
    safe_reports = 0

    for i, r in df.iterrows():
        if ordered_and_unique(r) and spaced_within(r, 3):
            safe_reports += 1

    print(safe_reports)

def ordered_and_unique(l: list) -> bool:
    l = [int(x) for x in l if x is not None]

    ordered = l == sorted(l) or l == sorted(l, reverse=True)
    unique = len(l) == len(set(l))

    return ordered and unique

def spaced_within(l: list, n: int) -> bool:
    l = [int(x) for x in l if x is not None]

    for i in range(1, len(l)):
        if abs(l[i] - l[i - 1]) > n:
            return False
    return True

if __name__ == '__main__':
    main()