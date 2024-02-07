import argparse 
import sys
import time 
from subprocess import run


parser = argparse.ArgumentParser()

parser.add_argument('accessions', help='')
parser.add_argument('regions', help='')
parser.add_argument('output', help='')
parser.add_argument('--test', required=False, action='store_true')
arg = parser.parse_args()

strains = []
with open(arg.accessions) as fp:
	for line in fp:
		l = line.split(',')
		strain = l[0]
		strains.append(strain)
strains = ','.join(strains[:5])
#print(strains)
#sys.exit()

#url = 'https://tools.1001genomes.org/api/v1/pseudogenomes'
url = 'https://tools.1001genomes.org/api/v1/vcfsubset/'

with open(arg.regions) as fp:
	counter = 0
	for line in fp:
		name, start, end, strand, lvl = line.split()
		if not name.endswith('.1'): continue 
		chrom = name[2]
		#curl = f'curl -X POST -d "strains={strains}&regions={chrom}:{start}..{end}" {url}'
		curl = f'curl -X POST {url} -d "strains={strains}&regions={chrom}:{start}-{end}&type=fullgenome&format=vcf"'
		print(curl)
		
		counter+=1
		if arg.test and counter >= 1: 
			break
		output = run(curl, shell=True, capture_output=True).stdout.decode()
		path = f'{arg.output}/{name}-{start}-{end}.fa'
		with open(path, 'w') as ofp:
			ofp.write(output)
			time.sleep(0.5)
		