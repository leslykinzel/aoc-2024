import pandas as pd

def main():
    with open('input.txt', 'r') as file:
        data = [line.split() for line in file.readlines()]

    longest_line = max(len(row) for row in data)

    for i in range(len(data)):
        while len(data[i]) < longest_line:
            data[i].append(None)

    df = pd.DataFrame(data)

    for i, r in df.iterrows():
        print(is_ordered_and_unique(r))

def is_ordered_and_unique(l: list) -> bool:
    l = [int(x) for x in l if x is not None]

    ordered = l == sorted(l) or l == sorted(l, reverse=True)
    unique = len(l) == len(set(l))

    return ordered and unique

def remove_item(l: list, s: str) -> list:
    return list(filter(lambda x: x != s, l))

if __name__ == '__main__':
    main()