import argparse
import pelops.py


parser = argparse.ArgumentParser(description="Find orthologous introns")
parser.add_argument("-f", "--filename", help="File to search for introns")
parser.add_argument("-k", "--kmer", default=3, help="Length of k-mer")
parser.add_argument("-x", "--shuffles", default=100, help="Number of shuffles")
parser.add_argument("-c", "--composition", default=[0.25, 0.25, 0.25, 0.25], help="Composition of nucleotides")


ortho_introns(args.filename, args.kmer, args.shuffles, args.composition)
