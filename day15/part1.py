import sys

#Frosting: capacity 4, durability -2, flavor 0, texture 0, calories 5
#Candy: capacity 0, durability 5, flavor -1, texture 0, calories 8
#Butterscotch: capacity -1, durability 0, flavor 5, texture 0, calories 6
#Sugar: capacity 0, durability 0, flavor -2, texture 2, calories 1

capacity = 0
durability = 0
flavor = 0
texture = 0
calories = 0
ingredients = {}
for line in sys.stdin:
	words = line.split()
	ingredients[words[0][:-1]] = (int(words[2][:-1]), int(words[4][:-1]), int(words[6][:-1]), int(words[8][:-1]), int(words[10]))
	
print(ingredients)

best = 0
for f in range(1,101):
	for c in range(1,101-f):
		for b in range(1,101-f-c):
			for s in range(1,101-f-c-b):
				cap = max(ingredients['Frosting'][0] * f + ingredients['Candy'][0] * c + ingredients['Butterscotch'][0] * b + ingredients['Sugar'][0] * s, 0)
				dur = max(ingredients['Frosting'][1] * f + ingredients['Candy'][1] * c + ingredients['Butterscotch'][1] * b + ingredients['Sugar'][1] * s, 0)
				fla = max(ingredients['Frosting'][2] * f + ingredients['Candy'][2] * c + ingredients['Butterscotch'][2] * b + ingredients['Sugar'][2] * s, 0)
				tex = max(ingredients['Frosting'][3] * f + ingredients['Candy'][3] * c + ingredients['Butterscotch'][3] * b + ingredients['Sugar'][3] * s, 0)
				cal = max(ingredients['Frosting'][4] * f + ingredients['Candy'][4] * c + ingredients['Butterscotch'][4] * b + ingredients['Sugar'][4] * s, 0)
				score = cap * dur * fla * tex
				
				### For part 2 ###
				if cal > 500:
					score = 0
				### end        ###
				
				if score > best:
					 best = score
					 
print(best)