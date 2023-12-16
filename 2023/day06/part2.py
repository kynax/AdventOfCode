with open('input.txt') as f:
    lines = [l.strip() for l in f]
    t = lines[0].replace(' ', '')
    d = lines[1].replace(' ', '')
    time = [int(i) for i in t.split(':') if 'Time' not in i ]
    distance = [int(i) for i in d.split(':') if 'Dist' not in i ]

    runs = 1
    for i in range(len(time)):
        t = time[i]
        d = distance[i]

        runs = runs * sum([1 for r in range(t) if r * (t-r) > d])
    
    print(runs)