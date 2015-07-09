seq = [1,2]
value = 0

while seq[-1] < 4000000:
	if seq[-1] % 2 == 0:
		value += seq[-1]
	seq.append(seq[-1] + seq[-2])

print value