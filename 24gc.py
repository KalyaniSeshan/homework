# 24gc.py

# Write a program that computes the GC% of a DNA sequence
# Format the output for 2 decimal places

dna = 'ACAGAGCCAGCAGATATACAGCAGATACTAT'
GC_number = 0

for i in range(len(dna)):
	nt = dna[i]
	if nt == 'C' or nt == 'G': GC_number += 1
	GC_percent = GC_number / len(dna)
print(f'{GC_percent:.2f}')

"""

python3 24gc.py
0.42

"""
