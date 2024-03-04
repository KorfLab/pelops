#mostly brainstorming
#test these individually 
#debug
#refgenome is the reference genome
#genomes are the test genomes aligned to the reference genome

import sys
import gzip


with open(sys.agv[1]) as fp:
	for line in fp:
		l = line.strip()
		
		


# find mismatch
mismatch(genomes, refgenome):
	mismatchs = {}
	for genome in genomes:
		for i in range(len(refgenome)):
				for j in range(len(genome)):
					if refgenome[i] != genome[j]:
						mismatchs[i] = genome[j]
	return mismatchs
	
						

# find the insertions form the genomes
getinsertions(genomes, refgenome):
	insertions = []
	for genome in genomes:
		for i in range(len(refgenome)):
			for j in range(len(genome))
		 		insertion = ''
		 			if refgenome[i] == 0:
		 				insertion += genome[j]
		 	insertions.append(insertion)
	return insertions
	
# find the deletions from the reference genome 		
getdeletions(genomes, refgenome):
	deletions = []
	for genome in genomes:
		for i in range(len(genome)):
			for j in range(len(refgenome))
		 		deletion = ''
		 			if genome[i] == '-':
		 				deletions += refgenome[j]
		 	deletions.append(deletion)
	return deletions
 
findlengths(seqs):
	lengths = []
	for seq in seqs:
		length = len(seq)
		lengths.append(length)
	return lengths
	
# find the positon of the insertions
inidx(incertions, genomes):
	inidx = {}
	for genome in genomes:
		for insertion in insertions:
			inpositions = []
			if insertion in genome:
				postion = find(insertion,genome,0)
			inpositions.append(position)
			inidx[insertion] = inpositions

# find the positon of the deletions
delidx(deletions, refgenome): 
	delidx = {}
	for deletion in deletions:
		delpostions = []
		if deletion in refgenome:
			postion = find(deletion, refgenome, 0)
		delpostions.apppend(postion)
		delidx[deletion] = delpostions
		

		