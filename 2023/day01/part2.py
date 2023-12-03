import sys
numl = ['zero','one','two','three','four','five','six','seven','eight','nine']
numr = ['z0o', 'o1e', 't2o','t3e', 'f4r', 'f5e', 's6x', 's7n', 'e8t', 'n9e']
nums = '0123456789'
total = 0
with open('input.txt', 'r') as f:
    for l in f:
        l = l.strip()
        for i in range(len(numl)):
            l = l.replace(numl[i], numr[i])

        num1 = None
        num2 = None
        for i in range(len(l)):
            if l[i] in nums and num1 is None:
                total = total + int(l[i]) * 10
                num1 = 1
            if l[-i-1] in nums and num2 is None:
                total = total + int(l[-i-1])
                num2 = 1
print(total)