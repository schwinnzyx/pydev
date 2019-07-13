"""
@Schwinn Zhang

Problem Description [source: Leetcode, https://leetcode.com/problems/generate-parentheses/]
22. Generate Parentheses
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:
[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
Add: valid input size >= 1
"""

# Method 1: Divide-N-Conquer
def generateParenthesisDNC(n: int):
	openp = '('
	closep = ')'
	hm = {}
	
	# base case n == 1
	hm[1] = [openp+closep]
	# null input
	if not n:
		return None

	if n == 1:
		return hm[1]
	
	for i in range(2,n+1):
		# case 1: prefix + postfix 
		for prefix_len in range(1,i):
			if i not in hm:
				hm[i] = [x+y for x in hm[prefix_len] for y in hm[i-prefix_len]]
			else:
				hm[i] += [x+y for x in hm[prefix_len] for y in hm[i-prefix_len] if x+y not in hm[i]]
		
		# case 2: (N-1)
		hm[i] += [openp + infix +closep for infix in hm[i-1]]
		
	return sorted(hm[n])

# Method 2: Backtrack
# Why backtrack? We are doing constrained satisfiability problem in a decision space
# Decision: whether to open or to close a parentheses
# Goal: n pair of well-formed parentheses
# Constraints: 1. exactly n open and n closed parentheses 2. can't close a parenthesis before an open one 

def generateParenthesisBacktrack(n:int):
	ans = []
	def backtrack(open_quota, closed_quota, prefix):
		if open_quota == 0 and closed_quota == 0:
			ans.append(prefix)
		if open_quota > 0:
			backtrack(open_quota-1, closed_quota, prefix + '(')
		if closed_quota > open_quota:
			backtrack(open_quota, closed_quota -1, prefix+')')
		 
	# kick off the backtrack decision tree    
	backtrack(n, n, '')
	return ans

if __name__ == "__main__":
	for input_n in range(1,5):
		print('Generate parenthesis for {} pairs using DNC method'.format(input_n))
		print(generateParenthesisDNC(input_n))
		print('Generate parenthesis for {} pairs using Backtrack'.format(input_n))
		print(generateParenthesisBacktrack(input_n))