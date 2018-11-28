def step(s):
    r = reversed(s)
    n = ''
    for c in r:
        n += '0' if c == '1' else '1'
    return s + '0' + n

def checksum(s):
    c = ''
    for i in range(len(s)//2):
        if s[i*2] == s[i*2+1]:
            c += '1'
        else:
            c += '0'
    if len(c) % 2 == 0:
        return checksum(c)
    return c

def fill(s,l):
    if len(s) > l:
        return s[:l]
    
    n = step(s)
    return fill(n,l)

# part 1
#print(checksum(fill('01111010110010011',272)))

# part 2
print(checksum(fill('01111010110010011',35651584)))