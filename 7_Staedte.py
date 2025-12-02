import itertools

dist = [
    [0, 101, 111, 114, 113, 140, 154],
    [101, 0, 125, 33, 64, 24, 76],
    [111, 125, 0, 150, 179, 139, 143],
    [114, 33, 150, 0, 33, 68, 106],
    [113, 64, 179, 33, 0, 85, 135],
    [140, 24, 139, 68, 85, 0, 83],
    [154, 76, 143, 106, 135, 83, 0]
]

cities = range(7)

best_route = None
best_distance = float("inf")

# Wir fixieren Stadt 0 als Startpunkt
for perm in itertools.permutations(cities[1:]):
    route = (0,) + perm + (0,)
    d = 0
    for i in range(len(route) - 1):
        d += dist[route[i]][route[i+1]]

    if d < best_distance:
        best_distance = d
        best_route = route

print("Beste Route:", best_route)
print("Distanz:", best_distance)
