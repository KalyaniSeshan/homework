# 41transmembrane.py

# Write a program that predicts which proteins in a proteome are transmembrane

# Transmembrane proteins are characterized by having
#    1. a hydrophobic signal peptide near the N-terminus
#    2. other hydrophobic regions to cross the plasma membrane

# Both the signal peptide and the transmembrane domains are alpha-helices
# Therefore, they do not contain Proline

# Hydrophobicity can be measured by Kyte-Dolittle
#	https://en.wikipedia.org/wiki/Hydrophilicity_plot

# For our purposes:
#	Signal peptide is 8 aa long, KD > 2.5, first 30 aa
#	Hydrophobic region is 11 aa long, KD > 2.0, after 30 aa

# Hint: copy mcb185.py to your homework repo and import that
# Hint: create a function for KD calculation
# Hint: create a function for hydrophobic alpha-helix
# Hint: use the same function for both signal peptide and transmembrane

import mcb185
import sys

def kd_hydro(aa):
	if aa == 'I': return 4.5
	if aa == 'V': return 4.2
	if aa == 'L': return 3.8
	if aa == 'F': return 2.8
	if aa == 'C': return 2.5
	if aa == 'M': return 1.9
	if aa == 'A': return 1.8
	if aa == 'G': return -0.4
	if aa == 'T': return -0.7
	if aa == 'S': return -0.8
	if aa == 'W': return -0.9
	if aa == 'Y': return -1.3
	if aa == 'P': return -1.6
	if aa == 'H': return -3.2
	if aa == 'E': return -3.5
	if aa == 'Q': return -3.5
	if aa == 'D': return -3.5
	if aa == 'N': return -3.5
	if aa == 'K': return -3.9
	if aa == 'R': return -4.5
	return 0
		
def a_helix(seq, w, t):
	hydro = 0
	for aa in seq:
		hydro += kd_hydro(aa)
	for i in range(len(seq) - w + 1):
		window = seq[i : i + w]
		if 'P' in window: 
			continue
		elif hydro / w < t: 
			continue
		else: 
			return True
	return False
		
for defline, seq in mcb185.read_fasta(sys.argv[1]):
	if a_helix(seq[0:30], 8, 2.5) and a_helix(seq[30:], 11, 2.0):
		print(defline)



"""
python3 41transmembrane.py ~/DATA/E.coli/GCF_000005845.2_ASM584v2_protein.faa.gz
NP_414560.1 Na(+):H(+) antiporter NhaA [Escherichia coli str. K-12 substr. MG1655]
NP_414568.1 lipoprotein signal peptidase [Escherichia coli str. K-12 substr. MG1655]
NP_414582.1 L-carnitine:gamma-butyrobetaine antiporter [Escherichia coli str. K-12 substr. MG1655]
NP_414607.1 DedA family protein YabI [Escherichia coli str. K-12 substr. MG1655]
NP_414609.1 thiamine ABC transporter membrane subunit [Escherichia coli str. K-12 substr. MG1655]
NP_414653.1 protein AmpE [Escherichia coli str. K-12 substr. MG1655]
NP_414666.1 quinoprotein glucose dehydrogenase [Escherichia coli str. K-12 substr. MG1655]
NP_414695.1 iron(III) hydroxamate ABC transporter membrane subunit [Escherichia coli str. K-12 substr. MG1655]
NP_414699.1 PF03458 family protein YadS [Escherichia coli str. K-12 substr. MG1655]
NP_414717.2 CDP-diglyceride synthetase [Escherichia coli str. K-12 substr. MG1655]
...
"""
