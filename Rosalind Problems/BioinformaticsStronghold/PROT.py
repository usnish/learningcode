# BIOINFORMATICS STRONGHOLD PROBLEM - Translating RNA into Protein
# Problem
# The 20 commonly occurring amino acids are abbreviated by using 20 letters from the English alphabet (all letters except for B, J, O, U, X, and Z). Protein strings are constructed from these 20 symbols. Henceforth, the term genetic string will incorporate protein strings along with DNA strings and RNA strings.
# The RNA codon table dictates the details regarding the encoding of specific codons into the amino acid alphabet.
# Given: An RNA string s corresponding to a strand of mRNA (of length at most 10 kbp).
# Return: The protein string encoded by s.
# Sample Dataset
# AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA
# Sample Output
# MAMAPRTEINSTRING

s = str(raw_input("RNA? :"))

#Went through a bit of a struggle to implement the codon table in an elegant way. Enter my bumbling solution:

codons = [ "GCU", "GCC", "GCA", "GCG", #A
	"CGU", "CGC", "CGA", "CGG", "AGA", "AGG", #R
	"AAU", "AAC", #N
	"GAU", "GAC", #D
	"UGU", "UGC", #C
	"CAA", "CAG", #Q
	"GAA", "GAG", #E
	"GGU", "GGC", "GGA", "GGG", #G
	"CAU", "CAC", #H
	"AUU", "AUC", "AUA", #I
	"UUA", "UUG", "CUU", "CUC", "CUA", "CUG", #L
	"AAA", "AAG", #K
	"AUG", #M
	"UUU", "UUC", #F
	"CCU", "CCC", "CCA", "CCG",  #P
	"UCU", "UCC", "UCA", "UCG", "AGU", "AGC", #S
	"ACU", "ACC", "ACA", "ACG", #T
	"UGG", #W
	"UAU", "UAC", #Y
	"GUU", "GUC", "GUA", "GUG", #V
	"UAA", "UGA", "UAG"]

aa = "AAAARRRRRRNNDDCCQQEEGGGGHHIIILLLLLLKKMFFPPPPSSSSSSTTTTWYYVVVV***"	

	#each codon in 'codons' corresponds directly to an amino acid in 'aa'; there are repeats so as to create a 1-to-1 mapping. Lazy, I know, but easy to understand.

print len(codons)

readstring = ""
prot = ""

for i in range(1,(len(s))/3+1):

	readstring = s[(i-1)*3:(i-1)*3+3]
	
	for j in range(0,len(codons)-1):
		if readstring == codons[j]:
			print readstring + " " + aa[j]
			prot += aa[j]

print prot

