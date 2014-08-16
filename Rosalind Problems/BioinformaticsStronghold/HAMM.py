# BIOINFORMATICS STRONGHOLD PROBLEM: COUNTING POINT MUTATIONS:
# Given: Two DNA strings s and t of equal length (not exceeding 1 kbp).
# Return: The Hamming distance dH(s,t).
# Sample Dataset
# GAGCCTACTAACGGGAT
# CATCGTAATGACGGCCT
# Sample Output
# 7

s = str(raw_input("DNA Strand 1? :"))
t = str(raw_input("DNA Strand 2? :"))

count = 0

for i in range(len(s)):
	if s[i] != t[i]:
		count += 1

print count