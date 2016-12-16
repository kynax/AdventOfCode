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
    s += Counter(letters[i]).most_common()[0][0]
print(s)