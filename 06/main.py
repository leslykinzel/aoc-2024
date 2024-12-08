import numpy as np

OBSTACLE = '#'
FOOTPRINT = 'X'

def main():
    with open('input.txt', 'r') as file:
        data = np.array([list(line.strip()) for line in file.readlines()])

    path_map = data.copy()

    initial_guard_pos = find_guard(path_map)
    initial_guard_state = path_map[initial_guard_pos[0], initial_guard_pos[1]]

    # Init guard obj
    guard = Guard(initial_guard_pos, initial_guard_state)

    ''' Part 1 - Count number of spaces visited by guard. '''

    while True:
        rc_guard = guard.position

        # Look ahead.
        rc_ahead = guard.next_position()
        if not is_within_bounds(path_map, rc_ahead):
            path_map[rc_guard[0], rc_guard[1]] = FOOTPRINT
            break

        ch_ahead = path_map[rc_ahead[0], rc_ahead[1]]
        if ch_ahead == OBSTACLE:
            guard.turn_right()

        # Move & leave footprint.
        path_map[rc_guard[0], rc_guard[1]] = FOOTPRINT
        guard.move_forward()

    print('Part 1:', np.count_nonzero(path_map == 'X'))

def find_guard(some_map: np.ndarray) -> tuple|None:
    for (row, col), val in np.ndenumerate(some_map):
        if val in ('^', '>', 'v', '<'):
            return (row, col)
    return None

def is_within_bounds(path_map: np.ndarray, position: tuple) -> bool:
    rows, cols = path_map.shape
    row, col = position
    return 0 <= row < rows and 0 <= col < cols

class Guard:

    def __init__(self, position: tuple, direction: str):
        self.position = position
        self.direction = direction

    def turn_right(self):
        match self.direction:
            case '^':
                self.direction = '>'
            case '>':
                self.direction = 'v'
            case 'v':
                self.direction = '<'
            case '<':
                self.direction = '^'

    def next_position(self):
        match self.direction:
            case '^':
                return (self.position[0]-1, self.position[1])
            case '>':
                return (self.position[0], self.position[1]+1)
            case 'v':
                return (self.position[0]+1, self.position[1])
            case '<':
                return (self.position[0], self.position[1]-1)

    def move_forward(self):
        self.position = self.next_position()


if __name__ == '__main__':
    main()