import re

def main():
    with open('example.txt', 'r') as file:
        raw = list(map(int, file.read().strip()))

    # print('Raw input:', raw)

    decoded = decode_diskmap(raw)
    print('Decoded:', decoded)

    # encoded = encode_diskmap(decoded)
    # print('Encoded:', encoded)

    # defrag = defrag_diskmap(decoded)
    # print('Defrag:', defrag)

    # checksum = calculate_checksum(defrag)
    # print('Checksum:', checksum)


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

def defrag_diskmap(diskmap: str) -> str:
    '''
        Integers swap positions with periods from right to left.
    '''
    charlist = list(diskmap)

    for i in range(len(charlist)-1, 0, -1):
        # print(''.join(charlist)) # [debug] view iteration
        if re.search(r'(?<=\.)\d', ''.join(charlist)):
            if charlist[i].isnumeric():
                for j in range(len(charlist)):
                    if charlist[j] == '.':
                        charlist[j], charlist[i] = charlist[i], charlist[j]
                        break
        else:
            break

    return ''.join(charlist)

def calculate_checksum(diskmap: str) -> int:
    '''
        Return sum of int[i] * i, ignores non ints.
    '''
    sum = 0

    for idx, val in enumerate(diskmap):
        if val.isnumeric():
            sum += int(val) * idx

    return sum

if __name__ == '__main__':
    main()
