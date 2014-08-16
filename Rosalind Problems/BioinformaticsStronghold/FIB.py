# BIOINFORMATICS STRONGHOLD PROBLEM #4: RABBITS AND RECURRENCE RELATIONS
# When finding the n-th term of a sequence defined by a recurrence relation, we can simply use the recurrence relation to generate terms for progressively larger values of n. This problem introduces us to the computational technique of dynamic programming, which successively builds up solutions by using the answers to smaller cases.
# Given: Positive integers n40 and k5.
# Return: The total number of rabbit pairs that will be present after n months if each pair of reproduction-age rabbits produces a litter of k rabbit pairs in each generation (instead of only 1 pair).
# Sample Dataset
# 5 3
# Sample Output
# 19

n = int(raw_input("n? :"))
k = int(raw_input("k? :"))

sequence = [0,1,1]
	# I'm lazy, okay?

for i in range(3,n+1):
	sequence.append(sequence[i-1] + sequence[i-2]*k)

print sequence[n]