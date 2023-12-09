with open('input.txt') as f:
    total = 0
    cards = [l.strip()[10:] for l in f]
    for c in cards:
        win,mine = c.split(' | ')
        win = [int(w) for w in win.split(' ') if w.strip() != '']
        mine = [int(w) for w in mine.split(' ') if w.strip() != '']
        cnt = sum([1 for m in mine if m in win])
        if cnt == 0:
            continue
        if cnt == 1:
            total = total + 1
        else:
            total = total + 2**(cnt-1)

    print(total)
        
