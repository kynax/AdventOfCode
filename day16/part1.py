import sys

sues = {}
real =  {'children': 3,'cats': 7,'samoyeds': 2,'pomeranians': 3,'akitas': 0,'vizslas': 0,'goldfish': 5,'trees': 3,'cars': 2,'perfumes': 1}

def gt(a,b):
	return a > b
def lt(a,b):
	return a < b
	
def compare(name,val):

	### BEGIN PART 2 ###
	if name in ['cats','trees']:
		return gt(val, real[name])
	if name in ['pomeranians', 'goldfish']:
		return lt(val, real[name])
	### END PART 2 ###
	return val == real[name]

for line in sys.stdin:
	words = line.split()
	
	if compare(words[2][:-1],int(words[3][:-1])) and compare(words[4][:-1], int(words[5][:-1])) and compare(words[6][:-1], int(words[7])):
		print(words[1][:-1])

