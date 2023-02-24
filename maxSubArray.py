nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

def maxSubArray(nums):
	res = nums[0]
	sum = 0
	for n in nums:
		sum += n
		res = max(res, sum)
		if sum < 0:
			sum = 0
	return res

print(maxSubArray(nums))
