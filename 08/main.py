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

def main():

    nodes = dict()
    antinodes = set()

    map_width = 0
    map_height = 0

    with open('input.txt', 'r') as file:
        for idx_y, line in enumerate(file):

            map_width = len(line.strip())

            for idx_x in range(len(line)):
                char = line[idx_x]

                if char == '.' or char == '\n':
                    continue

                if char not in nodes.keys():
                    nodes[char] = [(idx_x, idx_y)]
                else:
                    nodes[char].append((idx_x, idx_y))

            map_height+=1

    print(nodes, '\n')

    for _, coords in nodes.items():

        if len(coords) < 2: # there is no pair, skip
            continue

        for i in range(len(coords)):            # grab first in list
            for j in range(i + 1, len(coords)): # compare it to rest of list
                node_a = coords[i]
                node_b = coords[j]

                print(f'Checking: {node_a} in relation to: {node_b}')

                x_diff, y_diff = get_distance(node_a, node_b)

                print(f'Node A: {node_a} is ({x_diff}, {y_diff}) away from Node B: {node_b}')

                antinode_a = (node_a[0] - x_diff, node_a[1] - y_diff)
                antinode_b = (node_b[0] + x_diff, node_b[1] + y_diff)

                print(f'Antinode A: {antinode_a} -> in_bounds = {in_bounds(antinode_a, map_width, map_height)}')
                if in_bounds(antinode_a, map_width, map_height):
                    antinodes.add(antinode_a)

                print(f'Antinode B: {antinode_b} -> in_bounds = {in_bounds(antinode_b, map_width, map_height)}')
                if in_bounds(antinode_b, map_width, map_height):
                    antinodes.add(antinode_b)

                print()

    print('Part 1:', len(antinodes))

    '''
        Part 2: antinodes now go on forever at
        regular intervals, instead of just the
        ends of a pair of antennas.

        T....#....
        ...T......
        .T....#...
        .........#
        ..#.......
        ..........
        ...#......
        ..........
        ....#.....
        ..........
    '''

    antinode_rays = set()

    # yeah yeah DRY, idc
    for _, coords in nodes.items():

        if len(coords) < 2: # there is no pair, skip
            continue

        for i in range(len(coords)):
            for j in range(i + 1, len(coords)):
                node_a = coords[i]
                node_b = coords[j]

                x_diff, y_diff = get_distance(node_a, node_b)

                for c in range(-max(map_width, map_height), max(map_width, map_height)):
                    # c starts negative, so the addition here is symbolic
                    antinode = (node_a[0] + (c * x_diff), node_a[1] + (c * y_diff))

                    if in_bounds(antinode, map_width, map_height):
                        antinode_rays.add(antinode)

    print('Part 2:', len(antinode_rays))


def get_distance(node_a: tuple[int, int], node_b: tuple[int, int]) -> int:
    ''' Calculates distance between node_a and node_b. Does not give hypotenuse. '''
    x_diff = node_b[0] - node_a[0]
    y_diff = node_b[1] - node_a[1]
    return x_diff, y_diff

def in_bounds(node: tuple[int, int], x_limit: int, y_limit: int) -> bool:
    return 0 <= node[0] < x_limit and 0 <= node[1] < y_limit


if __name__ == '__main__':
    main()