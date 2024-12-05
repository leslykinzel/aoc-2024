
def main():
    with open('input.txt', 'r') as file:
        data = [list(line.strip()) for line in file]

    rows = len(data)
    cols = len(data[0])
    xmas = 0

    for r in range(rows):
        for c in range(cols):
            # Horizontal, normal
            if c + 3 < cols and data[r][c] == 'X' and data[r][c+1] == 'M' and data[r][c+2] == 'A' and data[r][c+3] == 'S':
                xmas += 1
            # Horizontal, backwards
            if c + 3 < cols and data[r][c] == 'S' and data[r][c+1] == 'A' and data[r][c+2] == 'M' and data[r][c+3] == 'X':
                xmas += 1
            # Vertical, normal
            if r + 3 < rows and data[r][c] == 'X' and data[r+1][c] == 'M' and data[r+2][c] == 'A' and data[r+3][c] == 'S':
                xmas += 1
            # Vertical, backwards
            if r + 3 < rows and data[r][c] == 'S' and data[r+1][c] == 'A' and data[r+2][c] == 'M' and data[r+3][c] == 'X':
                xmas += 1
            # Diagonal, NE
            if r + 3 < rows and c + 3 < rows and data[r][c] == 'X' and data[r+1][c+1] == 'M' and data[r+2][c+2] == 'A' and data[r+3][c+3] == 'S':
                xmas += 1
            # Diagonal, SW
            if r + 3 < rows and c + 3 < rows and data[r][c] == 'S' and data[r+1][c+1] == 'A' and data[r+2][c+2] == 'M' and data[r+3][c+3] == 'X':
                xmas += 1
            # Diagonal, SE
            if r - 3 >= 0 and c + 3 < cols and data[r][c] == 'S' and data[r-1][c+1] == 'A' and data[r-2][c+2] == 'M' and data[r-3][c+3] == 'X':
                xmas += 1
            # Diagonal, NW
            if r - 3 >= 0 and c + 3 < cols and data[r][c] == 'X' and data[r-1][c+1] == 'M' and data[r-2][c+2] == 'A' and data[r-3][c+3] == 'S':
                xmas += 1

    print(xmas)

if __name__ == '__main__':
    main()
