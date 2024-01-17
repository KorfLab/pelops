import random 
import sys
"""
seq = 'AAAAAAAAAAAAAAAAAAAA'
newseq = ''
n = random.randint(1,len(seq))
for j in range(len(seq)-n):
	newseq += 'A'
print(newseq, len(seq), len(newseq), n)
"""


seqs = []
iterations = 100
for i in range(iterations):
	length = random.randint(1,1000)
	seq = ''
	for j in range(length):
		seq += random.choice('ACGT')
	seqs.append(seq)
	
for seq in seqs:
	print('>', 'Name', '\n', seq)
	
	
#How to make alignments 
	#Maybe make a windowing algorithm of 10 or more and compare them
		#How to compare? 
		#If win1[j] == win2[j] 
			#add score +1
				#Append to dictionary 
				#Then add all .values
				#If alignment over threshold 
					#Get highest alignment 
					
				#Highest score is best alignment 
	#Maybe make my own blossom matrix?
		
	


#get the alignments for dummy sequences 
#find indels 
#find size of indels and make histograms for both
#pull sequence contents of the insertions
#What is the sequence content?
	
#get the alignments 
#if refgenome has sequence 