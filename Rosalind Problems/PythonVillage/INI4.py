#PYTHON VILLAGE PROBLEM #4: Conditions and Loops
#Given: Two positive integers a and b (a<b<10000).
#Return: The sum of all odd integers from a through b, inclusively.
#Sample Dataset
#100 200
#Sample Output
#7500

int1 = int(raw_input("int1? :"))
int2 = int(raw_input("int2? :"))

sum = 0

for i in range(int1, int2+1):
	if i%2 != 0:
		sum = sum + i

print sum