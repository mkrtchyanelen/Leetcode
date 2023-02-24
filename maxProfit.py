prices = [7, 1, 5, 3, 6, 4]

def maxProfit(prices):
	left = 0 #buy
	right = 1 #sell
	max_prf = 0

	while right < len(prices):
		current_prf = prices[right] - prices[left]
		if prices[right] > prices[left]:
			max_prf = max(current_prf, max_prf)
		else:
			left = right
		right += 1
	return max_prf

print(maxProfit(prices))
