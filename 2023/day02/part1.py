with open('input.txt') as f:
    total = 0
    for l in f:
        red = 12; green = 13; blue = 14 
        w = l.strip().split(': ')
        id = int(w[0][5:])
        games = w[1].split('; ')

        print(games)

        good = True
        for g in games:
            for p in g.split(', '):
                n, c = p.split(' ')
                if 'red' in c and int(n) > red:
                    good = False
                    #red = red - int(n)
                if 'green' in c and int(n) > green:
                    good = False
                    #green = green - int(n)
                if 'blue' in c and int(n) > blue:
                    good = False
                    #blue = blue - int(n)

        if good: #red >= 0 and blue >= 0 and green >= 0:
            print(id)
            total = total + id

print(total)