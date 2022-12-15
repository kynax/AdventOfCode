def compare(a,b):
    if isinstance(a, int) and isinstance(b,int):
        if a == b:
            return 0
        return (b - a) // abs(b-a)  # if a < b, good
    if isinstance(a,int) and not isinstance(b,int):
        return compare([a],b)
    if isinstance(b,int) and not isinstance(a,int):
        return compare(a, [b])
    
    # Compare the first value of each list, then the second value, and so on. 
    # If the left list runs out of items first, the inputs are in the right order. 
    # If the right list runs out of items first, the inputs are not in the right order. 
    # If the lists are the same length and no comparison makes a decision about the order, 
    #       continue checking the next part of the input.
    i = -1
    for i in range(len(b)):
        if i == len(a):
            return 1
        
        r = compare(a[i],b[i])

        if r == 0:
            continue
        else:
            return r
    
    if i < len(a)-1:
        return -1

    return 0


import sys
lines = [eval(l.strip()) for l in sys.stdin if l.strip() != '']
lines.append([[2]])
lines.append([[6]])

from functools import cmp_to_key
lines = sorted(lines, key=cmp_to_key(compare), reverse=True)
print((lines.index([[2]])+1) * (lines.index([[6]])+1))