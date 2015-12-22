import sys
import itertools

map = {}
depart = []
cities = []

for line in sys.stdin:
	distance = line.split(" = ")
	cities = distance[0].split(" to ")
	city1 = cities[0]
	city2 = cities[1]
	dist = int(distance[1])
	depart.append((city1,city2,dist))
	depart.append((city2,city1,dist))
	
	if city1 in map:
		map[city1][city2] = dist
	else:
		map[city1] = {city2 : dist}

	if city2 in map:
		map[city2][city1] = dist
	else:
		map[city2] = {city1 : dist}
	
best = 0
#best = 99999999
route = ""
for perm in itertools.permutations(map.keys()):
	dist = 0
	route = perm[0]
	for i in range(len(perm) -1):
		dist += map[perm[i]][perm[i+1]]
		route += " -> " + perm[i+1]
	if dist > best:
	#if dist < best:
		best = dist
		
print(best, route)