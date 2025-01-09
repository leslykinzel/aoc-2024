

def main():

    map_width = 0
    map_height = 0

    with open('example.txt', 'r') as file:
        data = list(line.strip() for line in file)

    # print(data)
    print(process_map(data))



def process_map(data: list[str]) -> list[tuple[int, tuple[int, int]]]:
    '''
        Processes 2d map into map of nodes: list[list[elevation, (x, y)]]
    '''
    node_map = list()

    for idx_y, row in enumerate(data):
        for idx_x, num in enumerate(row):
            node_map.append((int(num), (idx_x, idx_y)))

    return node_map


if __name__ == '__main__':
    main()
