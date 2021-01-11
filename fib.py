# You will have to figure out what parameters to include
# 🚨 All functions must use recursion 🚨

# This function returns the Nth number in the fibonacci sequence.
# https://en.wikipedia.org/wiki/Fibonacci_number
# For this function, the first two fibonacci numbers are 1 and 1
import functools

@functools.lru_cache(maxsize=128)

def fib(n):
	if type(n).__name__ != 'int':
		return "TypeError: Expected input of type 'int'. Instead got input of type '" + type(n).__name__ + "'."

	if n < 1:
		return 0
	if n < 3:
		return 1
	
	return fib(n - 1) + fib(n - 2)

print(fib(-1))
# => 0
print(fib(0))
# => 0
print(fib(1))
# => 1
print(fib(2))
# => 1
print(fib(7))
# => 13
print(fib('turtle'))