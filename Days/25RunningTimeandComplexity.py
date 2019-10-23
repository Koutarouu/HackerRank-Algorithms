from math import sqrt

def prime(n):
	if n==2: return "Prime"
	# 1 is not prime, even numbers > 2 are not prime
	if n==1 or (n&1) == 0:
		return "Not prime"
	for i in range(3, int(sqrt(n))+1, 2):
		if n%i==0:
			return "Not prime"
	return "Prime"

for _ in range(int(input())):
	print(prime(int(input())))

"""
Improved O( n^(1/2)) ) Algorithm
*Checks if n is divisible by 2 or any odd number from 3 to sqrt(n).
*The only way to improve on this is to check if n is divisible by 
*all KNOWN PRIMES from 2 to sqrt(n).

"""