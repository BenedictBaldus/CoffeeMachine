strecke = {
    'KO': {'PR':111, 'BI':114},
    'PR': {'MG':143,'BG':125},
    'BI': {'BG':106, 'OL':33,'MG':106},
    'MG': {'LEV':83},
    'BG': {'LEV':24},
    'OL': {'BG':64},
    'LEV': {}
         }

start = "KO"
unvisited = set ()
for node in strecke:
    unvisited.add(node)

distanzen = {}
for node in strecke:
    distanzen[node] = None
distanzen[start] = 0

print(unvisited)
print(distanzen)

while len(unvisited)>0:
    current = None
    for node in unvisited:
        if distanzen[node] is  None:
            current = node
    
        print(current)
    
    unvisited.remove(node)
