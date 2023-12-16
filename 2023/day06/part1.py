with open('input.txt') as f:
    lines = [l.strip() for l in f]
    t = lines[0]
    d = lines[1]
    time = [int(i) for i in t[5:].split(' ') if i != '' ]
    distance = [int(i) for i in d[9:].split(' ') if i != '' ]

    runs = 1
    for i in range(len(time)):
        t = time[i]
        d = distance[i]

        runs = runs * sum([1 for r in range(t) if r * (t-r) > d])
    
    print(runs)