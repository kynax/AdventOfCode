import sys

mol = 'CRnSiRnCaPTiMgYCaPTiRnFArSiThFArCaSiThSiThPBCaCaSiRnSiRnTiTiMgArPBCaPMgYPTiRnFArFArCaSiRnBPMgArPRnCaPTiRnFArCaSiThCaCaFArPBCaCaPTiTiRnFArCaSiRnSiAlYSiThRnFArArCaSiRnBFArCaCaSiRnSiThCaCaCaFYCaPTiBCaSiThCaSiThPMgArSiRnCaPBFYCaCaFArCaCaCaCaSiThCaSiRnPRnFArPBSiThPRnFArSiRnMgArCaFYFArCaSiRnSiAlArTiTiTiTiTiTiTiRnPMgArPTiTiTiBSiRnSiAlArTiTiRnPMgArCaFYBPBPTiRnSiRnMgArSiThCaFArCaSiThFArPRnFArCaSiRnTiBSiThSiRnSiAlYCaFArPRnFArSiThCaFArCaCaSiThCaCaCaSiRnPRnCaFArFYPMgArCaPBCaPBSiRnFYPBCaFArCaSiAl'
#mol = 'ZZSiZZZZSiZSiZZSi'
#mol = 'HOHOHO'
res = []
repl = []

for line in sys.stdin:
	words = line.split()
	repl.append((words[0],words[2]))

c = 0
for (key,val) in repl:
	cur = mol
	pre = ''
	while(key in cur):
		i = cur.index(key)
		out = pre + cur.replace(key,val,1)
		pre += cur[:i+1]
		cur = cur[i+1:]
		res.append(out)
#		if i == len(cur)-1:
#			break
		
print(len(set(res)))