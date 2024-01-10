import gzip

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

score, pct, qa, sa = read_bl2seq('example.blastn')

# example of how subs could be counted
change = {}
for q, s in zip(qa, sa):
	if q == s: continue
	if q == 'N' or s == 'N': continue
	if q not in change: change[q] = {}
	if s not in change[q]: change[q][s] = 0
	change[q][s] += 1

import json
print(json.dumps(change, indent=4))

