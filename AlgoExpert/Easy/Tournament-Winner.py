def tournamentWinner(competitions, results):
	outcome = {}
	
	for eachRound, result in zip(competitions, results):
		winner = eachRound[0] if result == 1 else eachRound[1]
		outcome[winner] = outcome.get(winner, 0) + 1
			
	#Get the key with the highest value
	return(max(outcome, key = outcome.get))