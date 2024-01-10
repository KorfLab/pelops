import gzip
import sys

def read_bl2seq(filename): # only tested for BLASTN
	if filename.endswith('.gz'):
		fp = gzip.open(filename, 'rt')
	else:
		fp = open(filename)
	
	score = None
	percent = None
	qalign = []
	salign = []
	
	for line in fp:
		f = line.split()
		if line.startswith(' Score'):
			if score: break # get the first alignment
			score = float(f[2])
		if line.startswith(' Identities'):
			n, l = f[2].split('/')
			percent = int(n) / int(l)
		if line.startswith('Query:'):
			qalign.append(f[2])
		if line.startswith('Sbjct:'):
			salign.append(f[2])
	fp.close()
	
	return score, percent, ''.join(qalign).upper(), ''.join(salign).upper()

def find_gaps(s1, s2):
	gapstrings = []
	off = 0
	while True:
		beg = s1.find('-', off)
		if beg == -1: break
		for end in range(beg +1, len(s1)):
			if s1[end] != '-': break
		off = end + 1
		gapstrings.append(s2[beg:end])
	return gapstrings


score, pct, qa, sa = read_bl2seq('gapped.blastn')
print(score, pct)

# example of how subs could be counted
change = {}
for q, s in zip(qa, sa):
	if q == s: continue
	if q == 'N' or s == 'N': continue
	if q == '-' or s == '-': continue
	if q not in change: change[q] = {}
	if s not in change[q]: change[q][s] = 0
	change[q][s] += 1

import json
print(json.dumps(change, indent=4))

# how to get gaps
print(find_gaps(qa, sa))
print(find_gaps(sa, qa))

# note that this is a simple method that doesn't take into account the
# phylogenetic relationships of the sequences: shared mutations will end
# double counted or worse. we shouldn't model all changes as independent
