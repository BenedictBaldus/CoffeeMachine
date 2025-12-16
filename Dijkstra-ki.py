strecke = {
    'KO': {'PR':111, 'BI':114},
    'PR': {'MG':143,'BG':125},
    'BI': {'BG':33, 'OL':33,'MG':106},
    'MG': {'LEV':83},
    'BG': {'LEV':24},
    'OL': {'BG':64},
    'LEV': {'':0}
         }

start = "KO"


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


print("Distanzen:", dist)
print("Vorgänger:", prev)


ziel = "LEV"
path = []
cur = ziel
while cur is not None:
    path.append(cur)
    cur = prev[cur]
path.reverse()

if path and path[0] == start:
    print("Pfad KO -> LEV:", path)
    print("Länge:", dist[ziel])
else:
    print("LEV ist von KO aus nicht erreichbar.")