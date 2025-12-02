dist = [
    [0, 101, 111, 114, 113, 140, 154],
    [101, 0, 125, 33, 64, 24, 76],
    [111, 125, 0, 150, 179, 139, 143],
    [114, 33, 150, 0, 33, 68, 106],
    [113, 64, 179, 33, 0, 85, 135],
    [140, 24, 139, 68, 85, 0, 83],
    [154, 76, 143, 106, 135, 83, 0]
]

n = 7
cities = list(range(n))
best_route = None
best_distance = float("inf")

def generate_permutations(arr, left, right, result):
    if left == right:
        copy_arr = arr.copy()
        result.append(copy_arr)
        return

    i = left
    while i <= right:
        temp = arr[left]
        arr[left] = arr[i]
        arr[i] = temp

        next_left = left + 1
        generate_permutations(arr, next_left, right, result)

        temp = arr[left]
        arr[left] = arr[i]
        arr[i] = temp

        i = i + 1

perm_base = cities[1:]
all_perms = []
generate_permutations(perm_base, 0, len(perm_base) - 1, all_perms)

for perm in all_perms:
    route = []
    route.append(0)

    j = 0
    while j < len(perm):
        route.append(perm[j])
        j = j + 1

    route.append(0)

    total_dist = 0
    k = 0
    while k < len(route) - 1:
        a = route[k]
        b = route[k + 1]
        total_dist = total_dist + dist[a][b]
        k = k + 1

    if total_dist < best_distance:
        best_distance = total_dist
        best_route = route

print("Beste Route:", best_route)
print("Distanz:", best_distance)
