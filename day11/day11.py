
def parse_input():
    with open("input.txt") as f:
        map= {}
        input = [line.strip().split(':') for line in f.readlines()]
        for node in input:
            map[node[0]] = tuple(node[1].split())

        return map

cache = {}
def possible_paths(graph, start_node, pass_dac, pass_fft):
    dac = pass_dac
    fft = pass_fft
    if start_node == 'dac':
        dac = True
    if start_node == 'fft':
        fft = True
    if 'out' in graph[start_node]:
        if pass_dac and pass_fft:
            return 1
        else:
            return 0
    elif (start_node, dac, fft) in cache:
        return cache[(start_node, dac, fft)]
    else:
        npaths = 0
        for next_node in graph[start_node]:
            npaths += possible_paths(graph, next_node, dac, fft)
        cache[(start_node, dac, fft)] = npaths
        return npaths

def main():
    graph = parse_input()
    print(possible_paths(graph, 'you', True, True))
    print(possible_paths(graph, 'svr', False, False))

main()
