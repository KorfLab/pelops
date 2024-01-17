import sys

genes = []
with open(sys.argv[1]) as fp:
	for line in fp:
		l = line.split()
		gene = l[0]
		if gene.endswith('.1'): genes.append(gene)
for gene in genes:
	print(gene)
	