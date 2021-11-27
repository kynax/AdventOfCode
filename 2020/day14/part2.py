
### Le code est à l'envers.
### Il faut appliquer le mask en premier, pour que les X écrasent les valeurs lorsque requis.
### Ensuite convertir tous les X en leurs 2 possibilités
def r_x(adr):
	if not 'X' in adr:
		yield adr
		
	for i in range(len(adr)):
		if adr[i] == 'X':
			#print(f'{adr} devient {adr[:i] + "?" + adr[i+1:]}')
			yield from r_x(adr[:i] + '0' + adr[i+1:])
			yield from r_x(adr[:i] + '1' + adr[i+1:])
			break
	
def applymask(adrb, mask):
	val = list(adrb)
	#print('conversion bin',val)
	new_val = []
	for i in range(len(mask)):
		if mask[i] == '0':
			new_val.append(val[i])
			continue

		new_val.append(mask[i])

	#print('appliquer le x sur', new_val)
	return list(r_x(''.join(new_val)))
	

			
			
def dict_print(dict):
	for k,v in dict.items():
		print(k, v)
			
								 
#val = 1
#adrb = '{0:036b}'.format(int(val))
#print('départ',adrb)
#mask = 'XX0000000000000000000000000000000000'
#for a in applymask(adrb, mask):
#	print('sortie',a)
#exit()
				  

import sys

mem = {}
mask = ''
for l in sys.stdin:
	if l.startswith('mask'):
		mask = l.split(' = ')[1].strip()
		continue
	
	[adr, val] = l.split(' = ')
	val = int(val)
	adr = int(adr[4:-1])
	adrb = '{0:036b}'.format(int(adr))
	
	for m in applymask(adrb, mask):
		#print(m, val)
		mem[m] = val
	#dict_print(mem)
	#print('')
	
#dict_print(mem)
	
print(sum([v for k,v in mem.items()]))