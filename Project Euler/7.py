#what is the 10001st prime number?
#this solution works, but it takes a good few minutes to run

def isprime(num):
	for x in range(2, num/2+1):
		if num % x == 0:
			return False
	return True



counter = 0
value = 0
number = 1
while counter != 10001:
	number += 1
	if isprime(number):
		counter += 1

print number


