# BIOINFORMATICS STRONGHOLD PROBLEM: COMPUTING GC CONTENT
# The GC-content of a DNA string is given by the percentage of symbols in the string that are 'C' or 'G'. For example, the GC-content of "AGCTATAG" is 37.5%. Note that the reverse complement of any DNA string has the same GC-content.
# DNA strings must be labeled when they are consolidated into a database. A commonly used method of string labeling is called FASTA format. In this format, the string is introduced by a line that begins with '>', followed by some labeling information. Subsequent lines contain the string itself; the first line to begin with '>' indicates the label of the next string.
# In Rosalind's implementation, a string in FASTA format will be labeled by the ID "Rosalind_xxxx", where "xxxx" denotes a four-digit code between 0000 and 9999.
# Given: At most 10 DNA strings in FASTA format (of length at most 1 kbp each).
# Return: The ID of the string having the highest GC-content, followed by the GC-content of that string. Rosalind allows for a default error of 0.001 in all decimal answers unless otherwise stated; please see the note on absolute error below.
# Sample Dataset
# >Rosalind_6404
# CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCCTCCCACTAATAATTCTGAGG
# >Rosalind_5959
# CCATCGGTAGCGCATCCTTAGTCCAATTAAGTCCCTATCCAGGCGCTCCGCCGAAGGTCTATATCCATTTGTCAGCAGACACGC
# >Rosalind_0808
# CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGACTGGGAACCTGCGGGCAGTAGGTGGAAT
# Sample Output
# Rosalind_0808
# 60.919540


inputfile = open('GC.txt','r')

lines = inputfile.readlines()
inputfile.close()

highest_id = ""
current_gc = 0.0
highest_gc = 0.0
current_id = ""
gc_count = 0.0
length = 0.0

debug = ""

for line in lines:
	if line[0] == '>':
		current_id = line[1:]
		current_gc = 0.0
		gc_count = 0.0
		length = 0.0


	else:
		#border case, where the last FASTA file doesn't end in a newline character, so the length is funky and throws off calculations
		if line[len(line) - 1] == 'A' or line[len(line) - 1] == 'C' or line[len(line) - 1] == 'G' or line[len(line) - 1] == 'T':
			length += len(line)
		else:
			length += len(line) - 1
		for i in line:
			if i == 'G' or i == 'C':
				gc_count += 1

		#cheap, lazy, and not entirely waterproof way of finding ending of DNA sequence; the probability of it fitting into perfect blocks of 60 is exceedingly low, and I'm not sure how to check for the ending of the sequence safely without getting an "Index out of range" error.
		if len(line) < 61:

			current_gc = gc_count / length * 100

			if current_gc > highest_gc:
				highest_gc = current_gc
				highest_id = current_id


print highest_id + str(highest_gc)



