for i in range(2,11):
    print(f"\n{i} table start\n")
    for j in range(1,11):
        print(f"{i} x {j} = {i*j}")
    ########
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def find_maxima(n, P):
    for i in range(n):
        maximal = True
        for j in range(n):
            if i != j and P[i].x <= P[j].x and P[i].y <= P[j].y:
                maximal = False
                break
        if maximal:
            print(f"Maximal point: ({P[i].x}, {P[i].y})")

# Example usage:
n = 5
points = [Point(1, 2), Point(2, 4), Point(1, 5), Point(1, 1), Point(2, 3)]
find_maxima(n, points)


##########
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def plane_sweep_maxima(n, P):
    P.sort(key=lambda point: point.x)  # Sort points in increasing order by x-coordinate
    s = []  # Stack to store maximal points

    for i in range(n):
        while s and s[-1].y <= P[i].y:
            s.pop()

        s.append(P[i])

    return s  # Return the stack of maximal points

# Example usage:
n = 5
points = [Point(1, 2), Point(2, 4), Point(1, 5), Point(1, 1), Point(2, 3)]
maximal_points = plane_sweep_maxima(n, points)

print("Maximal Points:")
for point in maximal_points:
    print(f"({point.x}, {point.y})")
