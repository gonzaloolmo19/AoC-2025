
def parse_input():
    with open("input.txt") as f:
        split = f.read().split('\n\n')
        ranges = [[int(elem) for elem in line.strip().split('-')] for line in split[0].strip().split('\n')]
        ids = [int(id) for id in split[1].strip().split('\n')]
        return ranges, ids

def part1():
    print(sum(map(lambda id: any(inf <= id <= sup for inf, sup in parse_input()[0]),parse_input()[1])))

def part2():
    ranges = map(lambda elem: [elem[0], elem[1]+1],sorted(parse_input()[0], key=lambda x: x[0]))
    count = 0
    current_max = 0
    for range in ranges:
        start = max(range[0], current_max)
        if start < range[1]:
            count += range[1] - start 
            current_max = range[1]
    print(count)

part1()
part2()

