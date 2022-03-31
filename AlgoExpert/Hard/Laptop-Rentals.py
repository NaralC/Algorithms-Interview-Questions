def laptopRentals(times):
    # Time: O(nlogn)
	# Space: O(n)
	
	# Gather the time which taking and returns are made
	timestamps = []
	
	for start, end in times:
		timestamps.append((start, 'start'))
		timestamps.append((end, 'end'))
	
	timestamps.sort()
	
	# Go through the timestamps chronologically
	laptop = output = 0
	
	for time, action in timestamps:
		if action == 'start':
			laptop += 1
		elif action == 'end':
			laptop -= 1
		
		output = max(output, laptop)
		
	return output