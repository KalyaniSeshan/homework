#!/usr/bin/env python3
# 50dust.py

# Write a better version of your 42dust.py program
# Your program must have the following properties

# 1. the entropy of each window is centered (N's in the middle of windows)
# 2. has option and default value for window size
# 3. has option and default value for entropy threshold
# 4. has a switch for N-based or lowercase (soft) masking
# 5. works with uppercase or lowercase input files
# 6. works as an executable --> needs executable permissions and an interpreter directive

# Optional: make the algorithm faster (see 29gcwin.py for inspiration)
# Optional: benchmark your programs with different window sizes using time

# Hint: make a smaller file for testing (e.g. e.coli.fna in the CLI below)

import mcb185
import math
import argparse

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
	
parser = argparse.ArgumentParser(description='50dust')
parser.add_argument('file', type=str, metavar='<path>', help='mcb185')
parser.add_argument('-w', '--window', required=False, type=int, default=11,
	metavar='<int>', help='optional string argument [%(default)i]')
# for option and default for window size
parser.add_argument('-t', required=False, type=float, default=1.4,
	metavar='<float>', help='optional floating point argument [%(default).1f]')
# option and default for entropy threshold
parser.add_argument('-n', action='store_true', help='mask with Ns')
parser.add_argument('--wrap', required=False, type=int, default=60,
	metavar='<int>', help='wrapping [%(default)i]') # use -- for full words
arg = parser.parse_args()
# print(arg) --> to test

for defline, seq in mcb185.read_fasta(arg.file):
	# mask sequence
	seq = seq.upper()
	seq1 = list(seq)
	for i in range(len(seq) - arg.window + 1):
		win = seq[i : i + arg.window]
		if seqent(win) < arg.t:
			for j in range(i, i + arg.window):
				if arg.n:
					seq1[j] = 'N'
				else: seq1[j] = seq[j].lower()
	# output sequence
	seq = ''.join(seq1)
	#print('>', defline, sep='')
	print(f'>{defline}')
	for i in range(0, len(seq), arg.wrap):
		print(seq[i:i+arg.wrap])

print(arg.file)

"""
python3 50dust.py -w 11 -t 1.4 -s e.coli.fna  | head
>NC_000913.3 Escherichia coli str. K-12 substr. MG1655, complete genome
AGCTTTTcATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTaaaaaaaGAGTGTC
TGATAGCAGCTTCTGAACTGGTTACCTGCCGTGAGTAAattaaaattttATTGACTTAGG
TCACTAAATacTTTAACCAATATAGGCATAGCGCACAGACAGAtAaaaaTTACAGAGTAC
ACAacATCCATGAAACGCATTAGCACCACCATTACCAccaccatCACCATTACCACAGGT
AACGGTGCgGGCTGACGCGTACAGGAAACacagaaaaAAGCCCGCACCTGACAGTGCGGG
CTttttttTTCGACCAAAGGTAACGAGGTAACAACCATGCGAGTGTTGAAGTTCGGCGGT
ACATCAGTGGCAAATGCAGAACGTTTTCTGCGTGTTGCCGATATTCTGGAAAGCAATGCC
AGGCAGggGCaGGTGGCCACCGTCcTCtctgcccCcgcCAAAatcaccaacCACCTGGTG
GCGATGATTGaAAAAacCATTAGCGGCCAGGATGCTTTACCCAATATCAGCGATGCCGAA

Timings
win alg1 alg2
11  28.7 25.8
25  30.4 26.1
100 33.2 26.1
200 37.4 25.9
"""
