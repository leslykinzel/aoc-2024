
def main():

    map_width = 0
    map_height = 0

    with open('example.txt', 'r') as file:
        grid = [list(map(int, line.strip())) for line in file.readlines()]

    node_grid = process_map(grid)
    starting_postitions = list()

    for line in node_grid:
        for node in line:
            if node.elevation == 0:
                starting_postitions.append(node)

    print(starting_postitions)



def process_map(grid: list[list[int]]) -> list[list]:
    ''' Transforms simple grid into grid of nodes. '''
    node_grid = list()

    for idx_y, line in enumerate(grid):
        node_line = list()
        for idx_x, num in enumerate(line):
            node_line.append(Node(num, idx_x, idx_y))

        node_grid.append(node_line)

    return node_grid


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
