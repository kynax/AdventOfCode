import sys

def mass(m):
    fuel = m // 3 - 2
    if fuel <= 0:
        return 0
    
    return fuel + mass(fuel) 

m = [mass(int(l.strip())) for l in sys.stdin]
print(sum(m))