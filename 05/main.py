
def main():
    with open('input.txt', 'r') as file:
        rules, jobs = file.read().strip().split('\n\n')

    rules = [tuple(map(int, l.split('|'))) for l in rules.splitlines()]
    jobs = [tuple(map(int, l.split(','))) for l in jobs.splitlines()]

    ps = PrintSorter(jobs, rules)
    valid_jobs = ps.get_valid_jobs()
    invalid_jobs = ps.get_invalid_jobs()

    ''' Part 1 - Find sum of each middle value in valid lists. '''

    part1 = []
    for job in valid_jobs:
        part1.append(job[len(job)//2])

    print('Part 1:', sum(part1))

    ''' Part 2 - Sort invalid lists, and find sum of each middle value. '''

    part2 = []
    for job in invalid_jobs:
        s_job = ps.sort_job(job)
        part2.append(s_job[len(s_job)//2])

    print("Part 2:", sum(part2))

class PrintSorter:

    def __init__(self, jobs: list[tuple[int]], rules: list[tuple[int]]):
        self.jobs = jobs
        self.rules = rules

    def is_corrupted(self, job: list[int]) -> bool:
        for x, y in self.rules:
            if x in job and y in job:
                if job.index(x) > job.index(y):
                    return True
        return False

    def get_valid_jobs(self) -> list[list[int]]:
        return [job for job in self.jobs if not self.is_corrupted(job)]

    def get_invalid_jobs(self) -> list[list[int]]:
        return [job for job in self.jobs if self.is_corrupted(job)]

    def sort_job(self, job: list[int]) -> list[int]:
        job_list = list(job)
        swap = True
        while swap:
            swap = False
            for x, y in self.rules:
                if x in job_list and y in job_list:
                    if job_list.index(x) > job_list.index(y):
                        job_list = self.swap_elements(job_list, x, y)
                        swap = True
        return job_list

    def swap_elements(self, job: list[int], x: int, y: int) -> list[int]:
        job_list = list(job)
        x_idx = job_list.index(x)
        y_idx = job_list.index(y)
        if x_idx > y_idx:
            job_list[x_idx], job_list[y_idx] = job_list[y_idx], job_list[x_idx]
        return job_list

if __name__ == '__main__':
    main()