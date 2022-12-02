import sys

i = ['.','A', 'B', 'C']

score = 0
for l in sys.stdin:
    theirs, res = l.strip().split(' ')
    theirs = i.index(theirs)

    if res == 'X': # loss:
        score += theirs - 1 if theirs > 1 else 3
    elif res == 'Y': # draw
        score += 3
        score += theirs
    else:
        score += 6
        score += theirs + 1 if theirs < 3 else 1

print(score)