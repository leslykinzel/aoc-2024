
def main():
    with open('input.txt', 'r') as file:
        # Need strip() to remove newline characters from map.
        data = [list(line.strip()) for line in file]

    rows = len(data)
    cols = len(data[0])
    
    for i in range(rows):
        for j in range(cols):
            pass

def out_of_bounds(x: int, y: int, n_rows: int, n_cols: int) -> bool:
    return x >= 0 and x <= n_rows and y >= 0 and y <= n_cols

if __name__ == '__main__':
    main()
