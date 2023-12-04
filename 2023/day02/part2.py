with open('input.txt') as f:
    total = 0
    for l in f:
        w = l.strip().split(': ')
        id = int(w[0][5:])
        games = w[1].split('; ')

        print(games)

        red = 0; green = 0; blue = 0 
        for g in games:
            for p in g.split(', '):
                n, c = p.split(' ')
                if 'red' in c and int(n) > red:
                    red = max(red, int(n))
                    #red = red - int(n)
                if 'green' in c and int(n) > green:
                    green = max(green, int(n))
                    #green = green - int(n)
                if 'blue' in c and int(n) > blue:
                    blue = max(blue, int(n))
                    #blue = blue - int(n)

        print(red, green, blue)
        total = total + red * blue * green

print(total)