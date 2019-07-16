
"""
@Schwinn Zhang
Permute a String by its characters using Backtracking
Thanks to: Standford CS106B by Marty Stepp 
"""
def permute(s):
	# check if input empty string
	if not s:
		return s

	alreadyPrinted = []
	return permuteHelper(s,"",alreadyPrinted)


def permuteHelper(s,chosen,alreadyPrinted):
	# base case: when no char left to permute 
	if not s:
		# check duplicates
		if chosen not in alreadyPrinted:
			global count
			count += 1
			alreadyPrinted.append(chosen)
			print(chosen)

	# use loop to select one char at a time
	for i in range(len(s)):
		# select a char
		char = s[i]
		chosen += char
		
		# build the next_s: aka remaining chars to choose from 
		# handle the right edge
		if i == len(s) -1:
			next_s = s[:i]
		else:
			next_s = s[:i] + s[i+1:]

		# explore/recurse
		permuteHelper(next_s,chosen, alreadyPrinted)

		# unchoose s[i]
		chosen = chosen[:-1]

if __name__ == "__main__":
	count = 0
	print("no duplicated chars in s:")
	permute('POKE')
	print("number of unique permutations of POKE:")
	print(count)
	print('\n')


	count = 0
	print("duplicated chars in s:")	
	permute('ROMEO')
	print("number of unique permutations of ROMEO:")
	print(count)




