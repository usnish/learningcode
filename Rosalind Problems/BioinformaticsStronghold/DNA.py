#COUNTING DNA NUCLEOTIDES
#Problem
# A string is simply an ordered collection of symbols selected from some alphabet and formed into a word; the length of a string is the number of symbols that it contains.
# An example of a length 21 DNA string (whose alphabet contains the symbols 'A', 'C', 'G', and 'T') is "ATGCTTCAGAAAGGTCTTACG."
# Given: A DNA string s of length at most 1000 nt.
# Return: Four integers (separated by spaces) counting the respective number of times that the symbols 'A', 'C', 'G', and 'T' occur in s.
# Sample Dataset
# AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC
# Sample Output
# 20 12 17 21

s = str(raw_input("Input DNA string? :"))

adenine = 0
cytosine = 0
guanine = 0
thymine = 0

for a in s:
	if a == 'A':
		adenine = adenine + 1

for c in s:
	if c == 'C':
		cytosine = cytosine + 1

for g in s:
	if g == 'G':
		guanine = guanine + 1

for t in s:
	if t == 'T':
		thymine = thymine + 1

print str(adenine) + ' ' + str(cytosine) + ' ' + str(guanine) + ' ' + str(thymine)

