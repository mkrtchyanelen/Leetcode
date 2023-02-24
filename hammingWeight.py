n = 11111111111111111111111111111111

def hammingWeight(n):

	sum = 0
	while n:
		n &= n-1
		sum += 1
	return sum

print(hammingWeight(n))
