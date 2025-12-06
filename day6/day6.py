from functools import reduce

def parse_input_part1():
    with open("input.txt") as f:
        input = [line.split() for line in f.readlines()]
        return [[input[j][i] for j in range(len(input))] for i in range(len(input[0]))]

def part1():
    counter = 0
    for problem in parse_input_part1():
        numbers = [int(num) for num in problem[:-1]]
        if problem[-1] == '+':
            counter += sum(numbers)
        else:
            counter += reduce(lambda x,y: x * y, numbers)
    print(counter)

def parse_input_part2():
    with open("input.txt") as f:
        input = f.readlines()
        transpose =[[input[j][i] for j in range(len(input))] for i in range(len(input[0]))]
        transpose = [reduce(lambda x, y: x+y, elem) for elem in transpose]
        operands = []
        last_i = 0
        for i in range(len(transpose)):
            if transpose[i].strip() == '':
                operands.append(transpose[last_i:i])
                last_i = i + 1
        operations = []
        for e in operands:
            operations.append(e[0][-1])
            e[0] = e[0][:-1]
            

        return [[int(e) for e in sub] for sub in operands], operations

def part2():
    operands, operations = parse_input_part2()
    counter = 0
    for i in range(len(operands)):
        if operations[i] == '+':
            counter += sum(operands[i])
        else:
            counter += reduce(lambda x,y: x*y, operands[i])
    print(counter)


    
part1()
part2()
