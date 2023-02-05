# 26anti.py

# Write a program that prints the reverse-complement of a DNA sequence
# You must use a loop and conditional

# Variation: try this with the range() function and slice syntax

dna = 'ACTGAAAAAAAAAAA'
revcomp = ''

for i in range(len(dna)):
	nt = dna[i]
	if nt == 'A': revcomp = 'T' + revcomp
	if nt == 'C': revcomp = 'G' + revcomp
	if nt == 'G': revcomp = 'C' + revcomp
	if nt == 'T': revcomp = 'A' + revcomp
print(revcomp)

"""
python3 26anti.py
TTTTTTTTTTTCAGT
"""
