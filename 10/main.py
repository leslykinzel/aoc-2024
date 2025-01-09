
def main():

    map_width = 0
    map_height = 0

    with open('example.txt', 'r') as file:
        data = list(line.strip() for line in file)

    print(process_map(data))


def process_map(data: list[str]) -> list[tuple[int, tuple[int, int]]]:
    '''
        Processes 2d map into map of nodes: list[list[elevation, (x, y)]]
    '''
    node_list = list()

    for idx_y, row in enumerate(data):
        for idx_x, num in enumerate(row):
            node_list.append(Node(num, idx_x, idx_y))

    return node_list

class Node:

    def __init__(self, elevation: int, x: int, y: int):
        self.elevation = elevation
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return f'({self.elevation}, ({self.x}, {self.y}))'

    def __eq__(self, value: tuple) -> bool:
        ''' compares the x and y coords of the node '''
        try:
            # expecting a tuple e.g. Node == (x, y)
            return self.x == value[0] and self.y == value[1]
        except IndexError:
            return False


if __name__ == '__main__':
    main()
