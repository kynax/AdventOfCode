#To continue, please consult the code grid in the manual.  Enter the code at row 2947, column 3029.

#              1,2,3, 4, 5, 6,...    2947
# row 1 goes : 1,3,6,10,15,21 ... 4343878

# col 2947 goes : .... 17850272

c = 1
inc = 2
for i in range(2,2947+1):
	c += inc
	inc += 1
for j in range(1,3029+1):
	c += i
	i += 1
print(c+1-i)

val = 20151125
for i in range(17850272+1):
	val *= 252533
	val = val % 33554393
	
print(val)