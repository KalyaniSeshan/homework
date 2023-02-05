# 25atseq.py

# Write a program that stores random DNA sequence in a string
# The sequence should be 30 nt long
# On average, the sequence should be 60% AT
# Calculate the actual AT fraction while generating the sequence
# Report the length, AT fraction, and sequence

# Note: set random.seed() if you want repeatable random numbers

import random 

#random.seed(10)

dna = ''
dna_length = 30
AT_fraction = 0.6
AT = 0

for i in range(dna_length):
	r = random.random()
	if r < AT_fraction:
		AT += 1
		dna += random.choice('AT')
	else: dna += random.choice('GC')
print(len(dna), AT / dna_length, dna)

"""
python3 25atseq.py
30 0.6666666666666666 ATTACCGTAATCTACTATTAAGTCACAACC
"""
