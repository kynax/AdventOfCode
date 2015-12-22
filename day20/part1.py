pz = 36000000


def prime_factors(n):
    i = 2
    factors = [1,n]
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return set(factors)
	
count = [0] * int(pz/10)
	
for elf in range(1,int(pz/10)):
	c = 0
	for house in range(elf,int(pz/10),elf):
		if c < 50:
			count[house] += elf * 11
			c += 1
		else:
			break
		
print("done counting")
for i in range(pz):
	if count[i] >= pz:
		print(i)
		break
print("done")