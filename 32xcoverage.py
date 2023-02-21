# 32xcoverage.py

# Write a program that simulates a shotgun resequencing project
# How uniformly do the reads "pile up" on a chromosome?
# How much of that depends on sequencing depth?

# Report min, max, and average coverage
# Make variables for genome size, read number, read length
# Input values from the command line

# Hint: make the problem smaller, so it's easier to visualize and debug
# Hint: if you don't understand the context of the problem, ask for help
# Hint: if you are undersampling the ends, do something about it

# Note: you will not get exactly the same results as the command line below

import sys
import random

genome = []
genome_size = int(sys.argv[1])
read_num = int(sys.argv[2])
read_len = int(sys.argv[3])

for i in range(genome_size):
	genome.append(0)

end = genome_size - read_len
for start in range(read_len):
	start = random.randint(0, end)
	for i in range(start, start + read_len):
		genome[i] += 1
		
minimum = genome[read_len: - read_len]
maximum = genome[read_len: - read_len]
avg_coverage = sum(genome[read_len: - read_len]) / len(genome)
print(min(minimum), max(maximum), f'{avg_coverage:.5f}')

"""
python3 32xcoverage.py 1000 100 100
5 20 10.82375
"""
