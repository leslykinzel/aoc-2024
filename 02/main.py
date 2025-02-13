import pandas as pd

def main():
    with open('input.txt', 'r') as file:
        data = [line.split() for line in file.readlines()]

    ''' Part 1 - Safe Reports '''

    df = pd.DataFrame(data)
    safe_reports = 0

    for _, r in df.iterrows():
        if ordered_and_unique(r) and spaced_within(r, 3):
            safe_reports += 1

    print('Part 1:', safe_reports)

    ''' Part 2 - Problem Dampener '''

    p2_safe_reports = 0

    for _, r in df.iterrows():
        r_vals = r.tolist()
        for n in range(len(r_vals)):
            r_combo = [val for j, val in enumerate(r_vals) if j != n]
            if ordered_and_unique(r_combo) and spaced_within(r_combo, 3):
                p2_safe_reports += 1
                break

    print('Part 2:', p2_safe_reports)

def ordered_and_unique(l: pd.Series) -> bool:
    l = [int(x) for x in l if x is not None]

    ordered = l == sorted(l) or l == sorted(l, reverse=True)
    unique = len(l) == len(set(l))

    return ordered and unique

def spaced_within(l: pd.Series, n: int) -> bool:
    l = [int(x) for x in l if x is not None]

    for i in range(1, len(l)):
        if abs(l[i] - l[i - 1]) > n:
            return False
    return True

if __name__ == '__main__':
    main()
