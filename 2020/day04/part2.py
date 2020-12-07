import sys
import string

def test(field, val):
	if field == 'byr':
		return int(val) >= 1920 and int(val) <= 2002
	if field == 'iyr':
		return int(val) >= 2010 and int(val) <= 2020
	if field == 'eyr':
		return int(val) >= 2020 and int(val) <= 2030
	if field == 'hgt':
		if val[-2:] == 'cm':
			return int(val[:-2]) >= 150 and int(val[:-2]) <= 193
		if val[-2:] == 'in':
			return int(val[:-2]) >= 59 and int(val[:-2]) <= 76
		return False
	if field == 'hcl':
		return len(val) == 7 and val[0] == '#' and all(c in string.hexdigits for c in val[1:])
	if field == 'ecl':
		return val in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth')
	if field == 'pid':
		return len(val) == 9 and val.isdigit()
	if field == 'cid':
		return True

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
		if all(test(k,v) for k,v in d.items()):
			total += 1	
		
print(total)