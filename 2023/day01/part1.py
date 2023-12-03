import sys
nums = '0123456789'
total = 0
with open('input.txt', 'r') as f:
    for l in f:
        l = l.strip()
        print(l)
        num1 = None
        num2 = None
        for i in range(len(l)):
            if l[i] in nums and num1 is None:
                print(l[i], " found, what index?")
                total = total + nums.index(l[i]) * 10
                num1 = 1
            if l[-i-1] in nums and num2 is None:
                print(l[-i-1], " found, what index?")
                total = total + nums.index(l[-i-1])
                num2 = 1
    print(total)
print(total)