from collections import deque

def main():

    part1 = 0
    part2 = 0

    with open('input.txt', 'r') as file:
        data = file.read().strip()

    grid = data.split('\n')

    rows = len(grid)
    cols = len(grid[0])

    for sr in range(rows):
        for sc in range(cols):
            if grid[sr][sc] == '0':
                queue = deque([(0, sr, sc)])
                seen = set()
                while queue:
                    d, r, c = queue.popleft()
                    if (r, c) in seen:
                        continue
                    seen.add((r, c))
                    if grid[r][c] == '9':
                        part1 += 1
                    for dr, dc in [(-1,0), (0,1), (1,0), (0,-1)]:
                        rr = r+dr
                        cc = c+dc
                        if 0<=rr<rows and 0<=cc<cols and int(grid[rr][cc]) == int(grid[r][c])+1:
                            queue.append((d+1, rr, cc))

    print(part1)


if __name__ == '__main__':
    main()
