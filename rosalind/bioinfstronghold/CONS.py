#Given a collection of at most 10 DNA Strings of equal length (at most 1 kbp) in FASTA format
#Return - A consensus string and profile matrix for the collection (If several possible consensus strings exist, then you may return any one of them)

import fileinput
sequences = []

for line in fileinput.input():
	if line[0] != '>':
		sequences.append(line.rstrip('\n'))

profile_matrix = {}
bases = ['A','C','G','T']
for x in bases:
	profile_matrix[x] = [0]*len(sequences[0])

for sequence in sequences:
	for pos in range(len(sequence)):
		profile_matrix[sequence[pos]][pos] += 1

print profile_matrix

for x in profile_matrix:


# PRINT OUTPUT
