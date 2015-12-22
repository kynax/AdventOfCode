import sys
import json

total = 0
js = None

for line in sys.stdin:
	js = json.loads(line)

def compute(j):
	total = 0
	if isinstance(j, dict):
		if 'red' in j.values():
			print(j, " ignored")
			return 0
		for obj in j.values():
			total += compute(obj)
	
	if isinstance(j, list):
		for obj in j:
			if isinstance(obj, int):
				total += obj
			else:
				total += compute(obj)
	if isinstance(j, int):
		total += j
		
	return total
	
print(compute(js))