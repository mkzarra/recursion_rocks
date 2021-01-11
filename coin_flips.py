# You will have to figure out what parameters to include
# 🚨 All functions must use recursion 🚨`

# This function returns an array of all possible outcomes from flipping a coin N times.
# Input type: Integer 
# H stands for Heads and T stands for tails
# Represent the two outcomes of each flip as "H" or "T"

def coin_flips(n):
	if n == 1:
		return ["T", "H"]

	already_flipped = coin_flips(n - 1)
	history_plus_heads = list(el + "H" for el in already_flipped)
	history_plus_tails = list(el + "T" for el in already_flipped)
	
	return history_plus_heads + history_plus_tails

print("two flips: ", coin_flips(2))
print("four flips: ", coin_flips(4))
# => ["HH", "HT", "TH", "TT"]