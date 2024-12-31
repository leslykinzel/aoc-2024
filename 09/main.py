
def main():
    with open('example.txt', 'r') as file:
        for line in file:
            raw = line.strip()

    print('Raw input:', raw)
    print('Decoded:', decode_diskmap(raw))

def decode_diskmap(raw: str) -> str:
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

if __name__ == '__main__':
    main()
