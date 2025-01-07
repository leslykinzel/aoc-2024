import re


def main():
    with open('input.txt', 'r') as file:
        raw = list(map(int, file.read().strip()))

    # print('Raw input:', raw)

    decoded = decode_diskmap(raw)
    # print(decoded)

    part1_defrag = defrag_diskmap(decoded)
    part1_checksum = calculate_checksum(part1_defrag)

    print('Part 1:', part1_checksum)

    part2_defrag = whole_file_defrag(raw)
    part2_checksum = calculate_whole_file_checksum(part2_defrag)

    print('Part 2:', part2_checksum)


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
    empty_indexes = [i for i, v in enumerate(disk) if v == -1]
    i = 0

    while True:
        while disk[-1] == -1: disk.pop()
        target = empty_indexes[i]
        if target >= len(disk):
            break
        disk[target] = disk.pop()
        i += 1

    return disk


def whole_file_defrag(disk: list) -> int:
    '''
        Whole file blocks attempt to fill empty spaces starting
        from idx[-1]. If they can't fill an empty space, move on
        to the next file block. 

        (file block == group of same int)
    '''
    isfile = True
    files = {}
    spaces = []
    ptr = 0

    for i, size in enumerate(disk):
        if isfile:
            files[i//2] = (ptr, size)
        else:
            spaces.append((ptr, size))
        isfile = not isfile
        ptr += size

    for id in reversed(files):
        loc, file_size = files[id]
        space_id = 0
        while space_id < len(spaces):
            space_loc, space_size = spaces[space_id]
            if space_loc > loc:
                break
            if space_size == file_size:
                files[id] = (space_loc, file_size)
                spaces.pop(space_id)
                break
            if space_size > file_size:
                files[id] = (space_loc, file_size)
                spaces[space_id] = (space_loc + file_size, space_size - file_size)
                break
            space_id += 1

    return files


def calculate_checksum(disk: list) -> int:
    '''
        Return sum of int[i] * i.
    '''
    return sum(i * val for i, val in enumerate(disk))


def calculate_whole_file_checksum(diskmap: dict) -> int:
    '''
        Return sum, expecting result of whole_file_defrag
    '''
    result = 0

    for id, (loc, size) in diskmap.items():
        for i in range(loc, loc + size):
            result += id * i

    return result


if __name__ == '__main__':
    main()
