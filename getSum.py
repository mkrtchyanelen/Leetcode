import math
a, b = 1, 2

def getSum(a, b):
	return math.log(2 ** a * 2 ** b, 2)

print(getSum(a, b))
