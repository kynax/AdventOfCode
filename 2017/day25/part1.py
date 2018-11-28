### example ###
checksum_at = 6
instructions = { 	'A': (	(1, 1, 'B'),
							(0, -1, 'B'),),
					'B': (	(1, -1, 'A'),
							(1, 1, 'A')) }
							
### part 1 ###
checksum_at = 12317297
instructions = { 	'A': (	(1, 1, 'B'),
							(0, -1, 'D')),
							
					'B': (	(1, 1, 'C'),
							(0, 1, 'F')),

					'C': (	(1, -1, 'C'),
							(1, -1, 'A')),

					'D': (	(0, -1, 'E'),
							(1, 1, 'A')),

					'E': (	(1, -1, 'A'),
							(0, 1, 'B')),

					'F': (	(0, 1, 'C'),
							(0, 1, 'E')) 
				}					

def read(i):
	if i not in tape:
		tape[i] = 0
	return tape[i]
def write(i, v):
	tape[i] = v

pos = 0
tape = {}
state = 'A'
	
for c in range(checksum_at):
	i = instructions[state][read(pos)]
	write(pos, i[0])
	pos += i[1]
	state = i[2]
	
print(sum(tape.values()))
