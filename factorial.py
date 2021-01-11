# You will have to figure out what parameters to include
# 🚨 All functions must use recursion 🚨

# This function returns the factorial of a given number.

def factorial(n):
	if n == 1:
		return n
		
	return n * factorial(n - 1)

print(factorial(5))
print(factorial(8))
# => 120