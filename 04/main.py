
def main():
    with open('input.txt', 'r') as file:
        data = [list(line.strip()) for line in file]

    rows = len(data)
    cols = len(data[0])
    part1 = 0
    part2 = 0


    for r in range(rows):
        for c in range(cols):
            ''' Part 1 - Find 'XMAS' in all directions, backwards and forwards. '''
            # Horizontal, normal
            if c + 3 < cols and data[r][c] == 'X' and data[r][c+1] == 'M' and data[r][c+2] == 'A' and data[r][c+3] == 'S':
                part1 += 1
            # Horizontal, backwards
            if c + 3 < cols and data[r][c] == 'S' and data[r][c+1] == 'A' and data[r][c+2] == 'M' and data[r][c+3] == 'X':
                part1 += 1
            # Vertical, normal
            if r + 3 < rows and data[r][c] == 'X' and data[r+1][c] == 'M' and data[r+2][c] == 'A' and data[r+3][c] == 'S':
                part1 += 1
            # Vertical, backwards
            if r + 3 < rows and data[r][c] == 'S' and data[r+1][c] == 'A' and data[r+2][c] == 'M' and data[r+3][c] == 'X':
                part1 += 1
            # Diagonal, NE
            if r + 3 < rows and c + 3 < rows and data[r][c] == 'X' and data[r+1][c+1] == 'M' and data[r+2][c+2] == 'A' and data[r+3][c+3] == 'S':
                part1 += 1
            # Diagonal, SW
            if r + 3 < rows and c + 3 < rows and data[r][c] == 'S' and data[r+1][c+1] == 'A' and data[r+2][c+2] == 'M' and data[r+3][c+3] == 'X':
                part1 += 1
            # Diagonal, SE
            if r - 3 >= 0 and c + 3 < cols and data[r][c] == 'S' and data[r-1][c+1] == 'A' and data[r-2][c+2] == 'M' and data[r-3][c+3] == 'X':
                part1 += 1
            # Diagonal, NW
            if r - 3 >= 0 and c + 3 < cols and data[r][c] == 'X' and data[r-1][c+1] == 'M' and data[r-2][c+2] == 'A' and data[r-3][c+3] == 'S':
                part1 += 1

            ''' Part 2 - Find 'MAS' in X shapes. '''
            if data[r][c] == 'A' and r - 1 >= 0 and r + 1 < rows and c - 1 >= 0 and c + 1 < cols:
                '''
                    M.M
                    .A.
                    S.S
                '''
                if data[r-1][c-1] == 'M' and data[r+1][c+1] == 'S':
                    if data[r+1][c-1] == 'S' and data[r-1][c+1] == 'M':
                        part2 += 1
                '''
                    S.S
                    .A.
                    M.M
                '''
                if data[r-1][c-1] == 'S' and data[r+1][c+1] == 'M':
                    if data[r+1][c-1] == 'M' and data[r-1][c+1] == 'S':
                        part2 += 1
                '''
                    M.S
                    .A.
                    M.S
                '''
                if data[r-1][c-1] == 'M' and data[r+1][c+1] == 'S':
                    if data[r+1][c-1] == 'M' and data[r-1][c+1] == 'S':
                        part2 += 1
                '''
                    S.M
                    .A.
                    S.M
                '''
                if data[r-1][c-1] == 'S' and data[r+1][c+1] == 'M':
                    if data[r+1][c-1] == 'S' and data[r-1][c+1] == 'M':
                        part2 += 1

    print('Part 1:', part1)
    print('Part 2:', part2)

if __name__ == '__main__':
    main()
