import sys

i = ['.','A', 'B', 'C']
o = ['.','X', 'Y', 'Z']

score = 0
for l in sys.stdin:
    theirs, mine = l.strip().split(' ')
    theirs = i.index(theirs)
    mine = o.index(mine)

    round = mine # my hand
    
    if mine == theirs: # draw
        round += 3
    elif (mine==1 and theirs==2) or (mine==2 and theirs==3) or (mine == 3 and theirs == 1): # loss
        round += 0
    else: # win
        round += 6

    score += round

print(score)