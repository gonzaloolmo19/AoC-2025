from functools import cache

def parse_input():
    with open("input.txt") as f:
        return [[char for char in line.strip()] for line in f.readlines()]

def down_propagation(diagram, initial_pos, visited_splitters):
    r, c = initial_pos 
    
    # Boundary check
    if (r < 0 or r >= len(diagram) or c < 0 or c >= len(diagram[0])):
        return
    
    # Traverse down
    while (r < len(diagram) and diagram[r][c] != '^'):
        r += 1
    
    # If we hit the bottom
    if r == len(diagram):
        return
        
    # We found a '^'
    current_pos = (r, c)
    if current_pos in visited_splitters:
        return

    visited_splitters.add(current_pos)
    
    down_propagation(diagram, (r, c-1), visited_splitters)
    down_propagation(diagram, (r, c+1), visited_splitters)

def quantum_down_propagation(diagram, initial_pos, cache):
    r, c = initial_pos
    
    # Boundary check
    if (r < 0 or r >= len(diagram) or c < 0 or c >= len(diagram[0])):
        return 1

    # Traverse down
    while (r < len(diagram) and diagram[r][c] != '^'):
        r += 1

    # If we hit the bottom
    if r == len(diagram):
        return 1
    
    # We found a '^'
    current_pos = (r,c)
    if current_pos in cache:
        return cache[current_pos]
    cache[current_pos]= quantum_down_propagation(diagram, (r, c-1), cache) + quantum_down_propagation(diagram, (r, c+1), cache)
    return cache[current_pos]

# Another using @cache decorator

@cache
def quantum_down_propagation2(diagram, initial_pos):
    r, c = initial_pos
    
    # Boundary check
    if (r < 0 or r >= len(diagram) or c < 0 or c >= len(diagram[0])):
        return 1

    # Traverse down
    while (r < len(diagram) and diagram[r][c] != '^'):
        r += 1

    # If we hit the bottom
    if r == len(diagram):
        return 1
    
    # We found a '^'
    return quantum_down_propagation2(diagram, (r, c-1)) + quantum_down_propagation2(diagram, (r, c+1))

def main():
    diagram = parse_input()
    initial_pos = next((i,j) for i, row in enumerate(diagram) for j, value in enumerate(row) if value == 'S')
    splits = set()
    down_propagation(diagram, initial_pos, splits)
    print(len(splits))
    cache = {}

    # It takes like 16 ms
    print(quantum_down_propagation(diagram, initial_pos, cache))

    # Using @cache is much slower than manually caching (220 ms)
    unmutable_diagram = tuple(tuple(row) for row in diagram)
    print(quantum_down_propagation2(unmutable_diagram, initial_pos))

main()
