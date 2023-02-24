n = 43261596

def reverseBits(n):
	binary = bin(n)[2:] #bin starts with 0b-slices 2

	rev = binary[::-1]
	reverse = rev.ljust(32, '0') #.ljust-pedding 0-s on the left till 32
	return int(reverse, 2)

print(reverseBits(n))
