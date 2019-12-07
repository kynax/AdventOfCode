def test(i):
    s = str(i)
    
    # Adjacent digits
    if not 0 in [int(s[j]) - int(s[j+1]) for j in range(len(s)-1)]:
        return False
    
    # Never decreases
    if list(s) != sorted(s):
        return False
    
    return True
    
c = 0
for i in range(273025,767253):
    if test(i):
        c += 1

print(c)