import sys
from collections import Counter

letters = []

for l in sys.stdin:
    if len(letters) == 0:
        for i in range(len(l)):
            letters.append([])
    for i in range((len(l))):
        letters[i].append(l[i])

s = ''
for i in range(len(letters)):
    d = Counter(letters[i]).most_common()
    s += d[len(d)-1][0]
    
print(s)