
def parse_input():
    with open("input.txt") as f:
        return [tuple([int(coord) for coord in line.strip().split(',')]) for line in f.readlines()]

def calculate_area(x, y):
    return (abs(x[0] - y[0])+1) * (abs(x[1] - y[1])+1)

def part2():
    vertices = parse_input()
    max_area = 0
    n = len(vertices)
    
    edges = []
    for i in range(n):
        p1 = vertices[i]
        p2 = vertices[(i + 1) % n]
        edges.append((p1, p2))

    # Iterate all pairs of vertices
    for i in range(n):
        for j in range(i + 1, n):
            p1 = vertices[i]
            p2 = vertices[j]
            
            # Define Rectangle Bounds
            min_x, max_x = min(p1[0], p2[0]), max(p1[0], p2[0])
            min_y, max_y = min(p1[1], p2[1]), max(p1[1], p2[1])
            
            area = calculate_area(p1, p2)
            
            if area <= max_area:
                continue

            # Validate the rectangle is valid
            is_valid = True
            
            # 1. Check for vertices strictly inside
            for v in vertices:
                if min_x < v[0] < max_x and min_y < v[1] < max_y:
                    is_valid = False
                    break
            if not is_valid:
                continue

            # 2. Check if an edge slices the rectangle
            for (ep1, ep2) in edges:
                # Vertical Edge Check
                if ep1[0] == ep2[0]: 
                    ex = ep1[0]
                    ey_min, ey_max = min(ep1[1], ep2[1]), max(ep1[1], ep2[1])
                    if min_x < ex < max_x and ey_min <= min_y and ey_max >= max_y:
                        is_valid = False
                        break
                # Horizontal Edge Check
                else: 
                    ey = ep1[1]
                    ex_min, ex_max = min(ep1[0], ep2[0]), max(ep1[0], ep2[0])
                    if min_y < ey < max_y and ex_min <= min_x and ex_max >= max_x:
                        is_valid = False
                        break
            if not is_valid:
                continue

            # 3. Now we know either the point is completely inside the polygon or completely outside.
            # We just need to check if one point is inside the polygon using raycasting
            mid_y = min_y + 0.5
            mid_x = min_x + 0.5
            intersections = 0
            for (ep1, ep2) in edges:
                edge_y_min, edge_y_max = min(ep1[1], ep2[1]), max(ep1[1], ep2[1])
                if edge_y_min < mid_y < edge_y_max:
                    # see if the edge is to the right
                    if ep1[0] > mid_x:
                        intersections += 1

            # We found new higher area
            if intersections % 2 == 1:
                max_area = area

    print(max_area)
   

def part1():
    points = parse_input()
    areas = []

    for i in range(len(points)):
        for j in range(i):
            areas.append(calculate_area(points[i], points[j]))
            
    print(max(areas))

part1()
part2()
