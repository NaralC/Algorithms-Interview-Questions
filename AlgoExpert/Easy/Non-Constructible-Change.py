def nonConstructibleChange(coins):
    coins.sort()
	accSum = 0
	
	for idx in range(len(coins)):
		if coins[idx] > accSum + 1: return accSum + 1
		else: accSum += coins[idx]
	
	return accSum + 1