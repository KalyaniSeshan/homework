# 42dust.py

# Write a program that performs entropy filtering on nucleotide fasta files
# Windows that are below the entropy threshold are replaced by N

# Program arguments include file, window size, and entropy threshold

# Output should be a fasta file with sequence wrapped at 60 characters

# Hint: use the mcb185 library
# Hint: make up some fake sequences for testing

# Note: don't worry about "centering" the entropy on the window (yet)

import mcb185
import sys
import math

def ent(vals):
	assert(math.isclose(sum(vals), 1.0))
	H = 0
	for val in vals:
		if val != 0: H -= val * math.log2(val)
	return H
	
def seqent(seq):
	A = seq.count('A') / len(seq)
	C = seq.count('C') / len(seq)
	T = seq.count('T') / len(seq)
	G = seq.count('G') / len(seq)
	H = ent([A, C, T, G])
	return H

w = int(sys.argv[2])
entthresh = float(sys.argv[3])

# print(w, entthresh) to test

for defline, seq in mcb185.read_fasta(sys.argv[1]):
	seq1 = list(seq)
	for i in range(len(seq)):
		if seqent(seq[i:i+w]) < entthresh:
			seq1[i] = 'N'
	seq = ''.join(seq1)
print(seq)

"""
		else:
			seq1 += seq[i]
	for i in range(0
	seq1 = 'N' + seq[i + 1 : i + w]
		

python3 42dust.py ~/DATA/E.coli/GCF_000005845.2_ASM584v2_genomic.fna.gz 11 1.4
>NC_000913.3 Escherichia coli str. K-12 substr. MG1655, complete genome
AGNTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTNNNNNNNAAAAAGAGTGTC
TGATAGCAGCTTCTGAACTGGTTACCTGCCGTGNNNNNNNNNNNATTTTATTGACTTAGG
TCACNNAATACTTTAACCAATATAGGCATAGCGCACAGNCNNNNAAAAATTACAGAGTNN
ACAACATCCATGAAACGCATTAGCACCACCATNNNNNNNACCATCACCATTACCACAGGT
AACNGTGCGGGCTGACGCGTACAGNNNNNNNNGAAAAAAGCCCGCACCTGACAGTGCNNN
NNNTTTTTTTCGACCAAAGGTAACGAGGTAACAACCATGCGAGTGTTGAAGTTCGGCGGT
ACATCAGTGGCAAATGCAGAACGTTTTCTGCGTGTTGCCGATATTCTGGAAAGCAATGCC
ANNCANGGGCAGGTGGCCANCGNNNNNNNTNNNCCCGNNNNNNNNNCCAACCACCTGGTG
GCGATNATTGNNAAAACCATTAGCGGCCAGGATGCTTTACCCAATATCAGCGATGCCGAA
...
"""
