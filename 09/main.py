import re

def main():
    with open('example.txt', 'r') as file:
        raw = list(map(int, file.read().strip()))

    # print('Raw input:', raw)

    decoded = decode_diskmap(raw)
    print('Decoded:', decoded)

    # encoded = encode_diskmap(decoded)
    # print('Encoded:', encoded)

    defrag = defrag_diskmap(decoded)
    print('Defrag:', defrag)

    checksum = calculate_checksum(defrag)
    print('Checksum:', checksum)


def decode_diskmap(raw: list) -> list:
    '''
        Decodes list of integer pairs into:

        - int 1 = n * i++
        - int 2 = n * '.'

        e.g. 2333 -> 00...111...
    '''
    disk = []

    for i in range(0, len(raw), 2):
        disk.extend(raw[i] * [i//2])
        if i + 1 < len(raw):
            disk.extend(raw[i+1] * [-1])

    return disk

def defrag_diskmap(disk: list) -> list:
    '''
        Integers swap positions with periods from right to left.
    '''
    empty_indexes = [idx for idx, val in enumerate(disk) if val == -1]
    i = 0

    while True:
        while disk[-1] == -1: disk.pop()
        target = empty_indexes[i]
        if target >= len(disk):
            break
        disk[target] = disk.pop()
        i += 1

    return disk

def calculate_checksum(disk: list) -> int:
    '''
        Return sum of int[i] * i.
    '''
    return sum(i * val for i, val in enumerate(disk))

if __name__ == '__main__':
    main()
