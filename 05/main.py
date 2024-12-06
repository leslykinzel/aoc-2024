from collections import defaultdict

def main():
    with open('input.txt', 'r') as file:
        rules, jobs = file.read().strip().split('\n\n')

    part1 = 0
    part2 = 0

    rules = [tuple(map(int, l.split('|'))) for l in rules.splitlines()]
    jobs = [tuple(map(int, l.split(','))) for l in jobs.splitlines()]

    ''' Part 1 - Sum middle values in correctly ordererd lists '''

    invalid_ordering = defaultdict(bool)
    for x, y in rules:
        invalid_ordering[y,x] = True

    def check_job(job):
        for i in range(len(job)):
            for j in range(i+1, len(job)):
                if invalid_ordering[job[i], job[j]]:
                    return 0
        return job[len(job)//2]

    for job in jobs:
        part1 += check_job(job)

    print('Part 1:', part1)

if __name__ == '__main__':
    main()