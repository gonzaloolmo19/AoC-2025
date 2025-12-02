import math

def parse_input():
    with open("input.txt") as f:
        return f.read().strip().split(',')

def invalid_number_part1(number):
    string = str(number)
    if len(string) % 2 == 1:
        return False
    left = string[:len(string)//2]
    right = string[len(string)//2:]
    return left == right
    
def part1():
    counter = 0
    for r in parse_input():
        split = r.split('-')
        for i in range(int(split[0]), int(split[1])+1):
            if invalid_number_part1(i):
                counter += i

    print(counter)

def get_div(numero):
    divisores = set()    
    limite = int(math.sqrt(numero))
    
    for i in range(1, limite + 1):
        if numero % i == 0:
            divisores.add(i)
            divisores.add(numero // i)
            
    return sorted(list(divisores))

def split_size(string, size):
    return [string[i:i+size] for i in range(0, len(string), size)]

def invalid_number_part2(number):
    string = str(number)
    divs = get_div(len(string))[:-1]
    for div in divs:
        split = split_size(string, div)
        if len(set(split)) == 1:
            return True
    return False

def part2():
    counter = 0
    for r in parse_input():
        split = r.split('-')
        for i in range(int(split[0]), int(split[1])+1):
            if invalid_number_part2(i):
                counter += i

    print(counter)

part1()
part2()
