def parse_input():
    with open("input.txt") as f:
        return [
            list(map(lambda x: 1 if x == "@" else 0, line.strip()))
            for line in f.readlines()
        ]


def part1():
    grid = parse_input()
    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                subgrid = list(
                    map(
                        lambda l: l[max(0, j - 1) : min(len(l), j + 2)],
                        grid[max(0, i - 1) : min(len(grid), i + 2)],
                    )
                )
                if sum(sum(row) for row in subgrid) < 5:
                    count += 1
    print(count)


def part2():
    grid = parse_input()
    count = 0
    eliminated = 1
    while eliminated != 0:
        eliminated = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    subgrid = list(
                        map(
                            lambda l: l[max(0, j - 1) : min(len(l), j + 2)],
                            grid[max(0, i - 1) : min(len(grid), i + 2)],
                        )
                    )
                    if sum(sum(row) for row in subgrid) < 5:
                        count += 1
                        eliminated += 1
                        grid[i][j] = 0
    print(count)


part1()
part2()
