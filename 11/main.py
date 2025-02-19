'''
    - If the stone is engraved with the number 0, it is replaced by a stone engraved with the number 1.

    - If the stone is engraved with a number that has an even number of digits, it is replaced by two stones. 
        The left half of the digits are engraved on the new left stone, and the right half of the digits are engraved 
        on the new right stone. (The new numbers don't keep extra leading zeroes: 1000 would become stones 10 and 0.)

    - If none of the other rules apply, the stone is replaced by a new stone; the old stone's number multiplied by 2024 is engraved on the new stone.

'''
from functools import cache

def main():
    with open('input.txt', 'r') as file:
        data = [int(n) for n in file.read().split()]

    ''' Part 1 - do 25 times '''

    print('Part 1:', do_x_times(25, data))

    ''' Part 2 - do 75 times, use faster algorithm '''

    print('Part 2:', sum(count(n, 75) for n in data))

@cache
def count(i: int, n: int) -> int:
    if n == 0:
        return 1
    if i == 0:
        return count(1, n-1)
    if even(len(str(i))):
        l, r = split_int(i)
        return count(l, n-1) + count(r, n-1)
    return count(i * 2024, n-1)

def do_x_times(x: int, original_data: list) -> int:
    l = original_data
    i = 0
    while i < x:
        t = blink(l)
        # print(len(t))
        l = t
        i += 1
    return len(t)

def blink(numbers: list) -> list:
    state = []
    for i in numbers:
        if i == 0:
            state.append(1)
        elif even(len(str(i))):
            l, r = split_int(i)
            state.append(l)
            state.append(r)
        else:
            state.append(i * 2024)
    return state

def even(n: int) -> bool:
    return n % 2 == 0

def split_int(n: int) -> int:
    s = str(n)
    l = len(s) // 2
    return int(s[:l + len(s) % 2]), int(s[l + len(s) % 2:])

if __name__ == '__main__':
    main()