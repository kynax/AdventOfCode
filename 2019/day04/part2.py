def test(i):
    s = str(i)
    
    # Only 2 adjacent digits
    ok = False
    for x in range(len(s)-1):
        if (s[x] == s[x+1] and # 2 adjacent
            (len(s) == x+2 or s[x+2] != s[x]) and # not same as previous 
            (x == 0 or s[x-1] != s[x])): # not same as next
            ok = True
    if not ok:
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