# stats are HP, DMG, AC
boss = (103,9,2)
me =   (100,0,0)

weapons = [
(8,4,0),
(10,5,0),
(25,6,0),
(40,7,0),
(74,8,0)
]

armors = [
(13,0,1),
(31,0,2),
(53,0,3),
(75,0,4),
(102,0,5)
]

rings = [
(25,1,0),
(50,2,0),
(100,3,0),
(20,0,1),
(40,0,2),
(80,0,3)
]

comb = [] # cost,dmg,ac

def fight(me,him):
	dmg = max(me[1] - him[2],1)
	him = (him[0] - dmg, him[1], him[2])
	if him[0] <= 0:
		return True
	dmg = max(him[1] - me[2],1)
	me = (me[0] - dmg, me[1], me[2])
	if me[0] <= 0:
		return False
	return fight(me,him)

for w in weapons:
	for a in armors:
		for r1 in rings:
			for r2 in rings:
				comb.append((w[0] + a[0] +  r1[0] + r2[0],w[1] + a[1] +  r1[1] + r2[1],w[2] + a[2] +  r1[2] + r2[2]))

best = 99999
win = True
### part 2
best = 0
win = False
###

for c in comb:
	if fight((me[0],me[1] + c[1], me[2] + c[2]),boss) == win:
		### part 2
		#if c[0] < best:
		if c[0] > best:
		###
			best = c[0]
print(best)