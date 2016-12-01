import sys
gates = {}

def compute(out):

	#print("Computing", out)

	if out.isdigit():
		#print("Digit -> Output :", out)
		gates[out] = int(out)
		return gates[out]
		
	gate = gates[out]
	
	if isinstance(gate, int):
		return int(gate)
	elif "AND" in gate:
		args = gate.split(" AND ")
		#print(args[0], " AND ", args[1], " -> Output :", out)
		gates[out] = compute(args[0]) & compute(args[1])
	elif "OR" in gate:
		args = gate.split(" OR ")
		gates[out] = compute(args[0]) | compute(args[1])
	elif "NOT" in gate:
		args = gate.replace("NOT ", "")
		gates[out] = ~ compute(args)  & 0xffff
	elif "LSHIFT" in gate:
		args = gate.split(" LSHIFT ")
		gates[out] = compute(args[0]) << compute(args[1])
	elif "RSHIFT" in gate:
		args = gate.split(" RSHIFT ")
		gates[out] = compute(args[0]) >> compute(args[1])
	else:
		gates[out] = compute(gate)
	return gates[out]
	

for g in sys.stdin:
	parts = g.strip().split(" -> ")
	gates[parts[1]] = parts[0]
#print(gates)
	
print(compute("a"))