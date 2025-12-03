
def parse_input():
    with open("input.txt") as f:
        return [[int(digit) for digit in line.strip()] for line in f.readlines()]

def max_joltage_part1(bank):
    argmax = bank.index(max(bank))
    if argmax != len(bank) - 1:
        return bank[argmax] * 10 + max(bank[argmax+1:])
    else:
        return max(bank[:-1]) * 10 + bank[argmax]

def part1():
    solution = 0
    for bank in parse_input():
        solution += max_joltage_part1(bank)
        
    print(solution)

def max_joltage_part2(bank):
    digits = []
    for i in range(11, -1, -1):
        if i == 0:
            argmax = bank.index(max(bank))
        else:
            argmax = bank.index(max(bank[:-i]))
        digits.append(bank[argmax])
        bank = bank[argmax+1:]
    sum = 0
    for i in range(0, 12):
        sum += digits[-i-1] * pow(10, i)
    return sum

def part2():
    solution = 0
    for bank in parse_input():
        solution += max_joltage_part2(bank)
        
    print(solution)
    

part1()
part2()
