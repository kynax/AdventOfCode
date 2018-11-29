import math
def prime(n):
    if n % 2 == 0 and n > 2: 
        return False
    return all(n % i for i in range(3, int(math.sqrt(n)) + 1, 2))

b = 107900
c = 124900
h = 0

for b in range(107900, c + 1, 17):
    if not prime(b):
        h += 1
		
print(h)