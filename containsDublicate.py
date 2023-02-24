nums = [1, 2, 3, 1]

def containsDublicate(nums):
	mydict = {}
	for i in nums:
		if i in mydict:
			return True
		mydict[i] = 1
	return False

print(containsDublicate(nums))
