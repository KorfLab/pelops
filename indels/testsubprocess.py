from subprocess import run
import time
import sys

#genes = run('python3 genes.py genes', shell=True, capture_output=True).stdout.decode().split('\n')
#strains = run('python3 strains.py accession.csv', shell=True, capture_output=True).stdout.decode().split('\n')
#print(strains[:-1])
#print(genes[:-1])

strains = []
with open(sys.argv[1]) as fp:
	for line in fp:
		l = line.split(',')
		strain = l[0]
		strains.append(strain)
	
genes = []
with open(sys.argv[2]) as fp:
	for line in fp:
		l = line.split()
		gene = l[0]
		if gene.endswith('.1'): genes.append(gene)	

strains = ",".join(strains[:100])
genes = genes[:100]

for gene in genes:
	print(gene, file=sys.stderr)
	for line in run(f'curl -X POST -d "strains={querystrains}&gids={querygenes}" https://tools.1001genomes.org/api/v1/pseudogenomes', shell=True, capture_output=True).stdout.decode().split('\n'):
		print(line)
		time.sleep(1)
