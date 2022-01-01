def removeIslands(matrix):
    #1) Traverse the border and mark all connected 1's as captured
	#2) Remove unconnected 1's
	#3) Converted connected 1's back to original
	for row in range(len(matrix)):
		for col in range(len(matrix[0])):
			if (row in [0, len(matrix) - 1] or col in [0, len(matrix[0]) - 1]
			   and matrix[row][col] == 1):
				markNeighbors(row, col, matrix)
				
	for row in range(len(matrix)):
		for col in range(len(matrix[0])):
			if matrix[row][col] == 1:
				matrix[row][col] = 0
	
	for row in range(len(matrix)):
		for col in range(len(matrix[0])):
			if matrix[row][col] == 'marked':
				matrix[row][col] = 1
				
	return matrix

def markNeighbors(row, col, matrix):
	#Boundary check
	if (row < 0 or row > len(matrix) - 1 or col < 0 or col > len(matrix[0]) - 1):
		return
	#Keep the capturing process inside the the island
	if matrix[row][col] != 1:
		return
	
	matrix[row][col] = 'marked'
	markNeighbors(row - 1, col, matrix)
	markNeighbors(row + 1, col, matrix)
	markNeighbors(row, col - 1, matrix)
	markNeighbors(row, col + 1, matrix)
				