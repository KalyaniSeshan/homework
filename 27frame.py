# 27frame.py

# Write a program that prints out the position, frame, and letter of the DNA

# Variation: try coding this with a single loop and nested loops

# Note: use 0-based indexing for position and frame (biology uses 1-based)

dna = 'ATGGCCTTT'

for i in range(len(dna)):
	nt = dna[i]
	if i in range(0, len(dna), 3):
		frame = 0
	elif i in range(1, len(dna), 3):
		frame = 1
	else: frame = 2
	print(i, frame, nt)	
		
"""
python3 27frame.py
0 0 A
1 1 T
2 2 G
3 0 G
4 1 C
5 2 C
6 0 T
7 1 T
8 2 T
"""
