import sys

l = sys.stdin.readline()

size = 25 * 6

layers = []
num_0 = 9999
score = 0

for layer in range(len(l) // size):
    values = [int(x) for x in l[layer * size : layer * size + size ]]
    zeros = values.count(0)
    if zeros < num_0:
        num_0 = zeros
        score = values.count(1) * values.count(2)
    layers.append(values)
    
    
print(score)
    