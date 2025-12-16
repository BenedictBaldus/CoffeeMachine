strecke = {
    'KO': {'PR':111, 'BI':114},
    'PR': {'MG':143,'BG':125},
    'BI': {'BG':33, 'OL':33,'MG':106},
    'MG': {'LEV':83},
    'BG': {'LEV':24},
    'OL': {'BG':64},
    'LEV': {} 
}

start = "KO"
ziel = "LEV"

unvisited = set()
for node in strecke:
    unvisited.add(node)

dist = {}
prev = {}
for node in strecke:
    dist[node] = None
    prev[node] = None

dist[start] = 0

while len(unvisited) > 0:
    current = None
    for node in unvisited:
        if dist[node] is not None:
            if current is None or dist[node] < dist[current]:
                current = node

    if current is None:
        break

    unvisited.remove(current)

    for neighbor in strecke[current]:
        if neighbor in unvisited:
            new_dist = dist[current] + strecke[current][neighbor]
            if dist[neighbor] is None or new_dist < dist[neighbor]:
                dist[neighbor] = new_dist
                prev[neighbor] = current

print("Länge:", dist[ziel])
