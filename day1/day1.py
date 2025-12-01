

def parse_input():
    with open("input.txt") as f:
        return f.read().split('\n')[:-1]

def part1():
    actions = parse_input()
    position = 50
    count = 0
    for action in actions:
        direction = 1 if action[0] == 'R' else -1
        step = int(action[1:])
        position = (position +(direction * step)) % 100
        if position == 0:
            count += 1

    print(count)

def part2():
    actions = parse_input()
    position = 50
    count = 0
    for action in actions:
        step = int(action[1:])
        if action[0] == 'L':
            raw_pos = position - step
            delta = step // 100
            if (position - step%100) <= 0:
                delta += 1
            if position == 0:
                delta -=1

        else:
            raw_pos = position + step
            delta = (position + step) // 100

        count += delta
        print (position, action, delta)
        position = raw_pos % 100

    print(count)


part1()
part2()

