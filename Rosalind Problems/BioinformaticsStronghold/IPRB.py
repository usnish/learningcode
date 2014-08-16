# BIOINFORMATICS STRONGHOLD PROBLEM: MENDEL'S FIRST LAW
# Given: Three positive integers k, m, and n, representing a population containing k+m+n organisms: k individuals are homozygous dominant for a factor, m are heterozygous, and n are homozygous recessive.
# Return: The probability that two randomly selected mating organisms will produce an individual possessing a dominant allele (and thus displaying the dominant phenotype). Assume that any two organisms can mate.
# Sample Dataset
# 2 2 2
# Sample Output
# 0.78333

AA = float(raw_input("AA :"))
Aa = float(raw_input("Aa :"))
aa = float(raw_input("aa :"))

population = AA + Aa + aa

# two AA
AAAA = AA/population * (AA - 1)/(population - 1) * 1
# two Aa 
AaAa = Aa/population * (Aa - 1)/(population - 1) * 3/4
# two aa
aaaa = aa/population * (aa - 1)/(population - 1) * 0
# AA + Aa
AAAa = AA/population * Aa/(population - 1) * 1
# AA + aa
AAaa = AA/population * aa/(population - 1) * 1
# Aa + aa
Aaaa = Aa/population * aa/(population - 1) * 1/2
# Aa + AA
AaAA = Aa/population * AA/(population - 1) * 1
# aa + AA
aaAA = aa/population * AA/(population - 1) * 1
# aa + Aa
aaAa = aa/population * Aa/(population - 1) * 1/2

finalprob = AAAA + AaAa + aaaa + AAAa + AAaa + Aaaa + AaAA + aaAA + aaAa

print finalprob