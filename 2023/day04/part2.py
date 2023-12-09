total = 0
with open('input.txt') as f:
    total = 0
    cards = [l.strip()[l.strip().index(':')+2:] for l in f]
    numcards = [1] * len(cards)
    for i in range(len(numcards)):
        win,mine = cards[i].split(' | ')
        win = [int(w) for w in win.split(' ') if w.strip() != '']
        mine = [int(w) for w in mine.split(' ') if w.strip() != '']
        cnt = sum([1 for m in mine if m in win])
        for x in range(cnt):
            numcards[i+x+1] = numcards[i+x+1] + numcards[i]

    print(sum(numcards))
        
