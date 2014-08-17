def ispal(number):
	half = len(str(number)) // 2
	left = str(number)[:half]
	if len(str(number)) % 2 == 0:
		right = str(number)[half:]
		right = right[::-1]
	else:
		right = str(number)[half+1:]
		right = right[::-1]
	return left == right

value = 0

for i in range(999,100,-1):
	for j in range(999,100,-1):
		if ispal(i*j):
			if i*j > value:
				value = i*j

print value




