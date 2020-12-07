import sys

vals = []
dicts = []
for l in sys.stdin:
	if len(l.strip()) == 0:
		d = {}
		for kv in vals:
			k,v = kv.split(':')
			d[k] = v
		dicts.append(d)
		vals = []
		continue
		
	vals.extend( l.strip().split(' ') )

total = 0
reqs = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'] #, 'cid' ]
for d in dicts:
	result =  all(elem in d.keys() for elem in reqs)
	if result:
		total += 1
		
print(total)