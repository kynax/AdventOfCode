import sys

cwd = ''
files = []
dirs = ['/']
lines = [l.strip() for l in sys.stdin]

for i in range(len(lines)):
    if '$ cd /' == lines[i]:
        cwd = '/'
        continue

    if '$ cd ..' == lines[i]:
        cwd = '/'.join(cwd.split('/')[:-2]) + '/'
        continue

    if '$ cd' in lines[i]:
        cwd += lines[i][5:] + '/'
        if cwd not in dirs:
            dirs.append(cwd)
        continue

    if '$ ls' == lines[i]:
        while i+1 < len(lines) and lines[i+1][0] != '$':
            i += 1
            if lines[i][0] == 'd':
                continue
            size, file = lines[i].split(' ')
            files.append( (cwd+file, int(size)) )

total = 0
for f in files:
    total += f[1]

print(30000000 - (70000000 - total), 'extra space required')

best = 9999999999999
b_dir = ''
for d in dirs:
    sum = 0
    for f in files:
        if d in f[0]:
            sum += f[1]
    
    if sum <= best and sum > 30000000 - (70000000 - total):
        best = sum
        b_dir = d

print(b_dir, best)