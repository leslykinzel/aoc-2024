
def main():
    with open('input.txt', 'r') as file:
        data = [list(c.strip()) for c in file.readlines()]

    print(data)

if __name__ == '__main__':
    main()
