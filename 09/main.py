import re

def main():
    with open('example.txt', 'r') as file:
        for line in file:
            raw = line.strip()

    # print('Raw input:', raw)

    decoded = decode_diskmap(raw)
    print('Decoded:', decoded)

    # encoded = encode_diskmap(decoded)
    # print('Encoded:', encoded)
    defrag = defrag_diskmap(decoded)
    print('Defrag:', defrag)

    checksum = calculate_checksum(defrag)
    print('Checksum:', checksum)


def decode_diskmap(raw: str) -> str:
    '''
        Decodes sequence of integer pairs into:

        - int 1 = n * i++
        - int 2 = n * '.'

        e.g. 2333 -> 00...111...
    '''
    result = ''
    id = 0

    for idx, val in enumerate(raw):
        if idx % 2 == 0:
            # file data
            for _ in range(int(val)):
                result += str(id)
            id+=1
        else:
            # blank space
            for _ in range(int(val)):
                result += '.'

    return result

def encode_diskmap(map_string: str) -> str:
    '''
        RLE encoding that expects pairs of values,
        reversing the process in decode_diskmap.
    '''
    result = ''
    stack = []

    for val in map_string:
        if stack and stack[-1] != val:
            result += f'{len(stack)}{'0' if stack[-1].isnumeric() and val.isnumeric() else ''}'
            stack.clear()
        stack.append(val)

    if stack:
        result += str(len(stack))

    return result

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
