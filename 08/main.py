'''
    ..........
    ...#......
    ..........
    ....a.....
    ..........
    .....a....
    ..........
    ......#...
    ..........
    ..........

    - Antinodes occur at any point that is perfectly in 
      line with two antennas of the same frequency.

      They only occur on the outer bounds of a pair of 
      antennas; and the distance between each antenna
      dictates the distance of the antinodes.

    ..........
    ...#......
    #.........
    ....a.....
    ........a.
    .....a....
    ..#.......
    ......#...
    ..........
    ..........

    - Antinodes cannot appear out of bounds.

    ..........
    ...#......
    #.........
    ....a.....
    ........a.
    .....a....
    ..#.......
    ......A...
    ..........
    ..........

    - Antinodes with different frequencies do not create
      antinodes. However, they can obstruct any location
      that does contain an antinode. (These are still counted)

    example.txt contains 14 antinodes.

'''
from dataclasses import dataclass
import math

def main():

    nodes = list()

    map_width = 0
    map_height = 0

    with open('example.txt', 'r') as file:
        for idx_y, line in enumerate(file):

            map_width = len(line)
            print(line)

            for idx_x in range(len(line)):
                char = line[idx_x]

                if char == "." or char == "\n":
                    continue

                nodes.append(Node(char, idx_x, idx_y))


        map_height+=1

    print(nodes)


@dataclass(frozen=True)
class Node:

    id: str
    x: int
    y: int

    def position(self) -> tuple[int, int]:
        return tuple(self.x, self.y)

    def get_distance(self, pos: tuple[int, int]) -> int:
        ''' Calculates distance between this and another Node '''
        x_diff = self.x - pos[0]
        y_diff = self.y - pos[1]
        return x_diff, y_diff

    def __str__(self) -> str:
        return f'{self.id}: ({self.x}, {self.y})'


if __name__ == '__main__':
    main()