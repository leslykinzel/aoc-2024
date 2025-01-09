
def main():

    part2 = 0

    with open('input.txt', 'r') as file:
        data = file.read().strip()

    grid = data.split('\n')

    rows = len(grid)
    cols = len(grid[0])

    dp = {}

    def ways(r, c):
        if grid[r][c] == '0':
            return 1
        if (r, c) in dp:
            return dp[(r, c)]
        ans = 0
        for dr, dc in [(-1,0), (0,1), (1,0), (0,-1)]:
            rr = r+dr
            cc = c+dc
            if 0<=rr<rows and 0<=cc<cols and int(grid[rr][cc]) == int(grid[r][c])-1:
                ans += ways(rr, cc)
        dp[(r, c)] = ans
        return ans

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '9':
                part2 += ways(r, c)

    print(part2)


if __name__ == '__main__':
    main()
