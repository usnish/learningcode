# BIOINFORMATICS STRONGHOLD PROBLEM #3: COMPLEMENTING A STRAND OF DNA
# Problem
# In DNA strings, symbols 'A' and 'T' are complements of each other, as are 'C' and 'G'.
# The reverse complement of a DNA string s is the string sc formed by reversing the symbols of s, then taking the complement of each symbol (e.g., the reverse complement of "GTCA" is "TGAC").
# Given: A DNA string s of length at most 1000 bp.
# Return: The reverse complement sc of s.
# Sample Dataset
# AAAACCCGGT
# Sample Output
# ACCGGGTTTT

s = str(raw_input("Input DNA Strand:"))
o = ''

for i in s:
	if i == 'A':
		o = o + 'T'
	if i == 'C':
		o = o + 'G'
	if i == 'G':
		o = o + 'C'
	if i == 'T':
		o = o + 'A'

	#What a pretty pattern of equal signs...

o = o[::-1]
	#extended slice, reverses string in a short space of code

print o