# Find Orthologous Introns

import argparse
import random
import math

# maybe make parser take a json file??
# comp is [A, C, G, T]
args = parser.parse_args()

def point_mutations(seq, prob=0.01):
    # can add a version that guarantees a certain percentage of mutations
    seq = list(seq)
    nuc = ['A', 'C', 'G', 'T']
    for i in range(len(seq)):
        if(random.random() < prob):
            seq[i] = random.choice(nuc)
    seq = "".join(seq)
    return seq

def frame_shift(seq, prob=0.01):
    nuc = ['A', 'C', 'G', 'T']
    for i in range(len(seq)):
        if(random.random() < prob):
            # deletion
            seq = seq[:i] + random.choice(nuc) + seq[i:]
    return seq

def randomize_seq(seq):
    seq = list(seq)
    random.shuffle(seq) # doesn't work
    return "".join(seq)

def reverse_complement(seq):
    reverse_seq = seq[::-1]
    reverse_seq = reverse_seq.replace('A', 'T')
    reverse_seq = reverse_seq.replace('T', 'A')
    reverse_seq = reverse_seq.replace('C', 'G')
    reverse_seq = reverse_seq.replace('G', 'C')
    # I feel like there's an re function that does this (elegantly)
    return reverse_seq

def kmer_shuffle_sampling(seq, k):
    child = ""
    while len(child) < len(seq):
        position = random.randint(0, len(seq) - k)
        child += seq[position:position+k]
    return child[:len(seq)]

# Make gzip later

def ortho_introns(filename, k, x, comp=[0.25, 0.25, 0.25, 0.25]):
    # read fasta file
    with open(filename, 'r') as f:
        lines = f.readlines()
        headers = []
        seqs = []
        seq = ""
        for line in lines:
            if line.startswith('>') and line != "" : 
                headers.append(line.strip())
                seqs.append(seq)
                seq = ""
            else:            
                seq += line.strip()
        seqs.append(seq)
        seqs = seqs[1:]

# get nuc composition of each sequence
    kmer_ls = []
    shuffled = {seq: [] for seq in seqs}
    score = []
    for header, seq in zip(headers, seqs):
        for i in range(x): 
            for j in range(len(seq) - k + 1):
                kmer_ls.append(seq[j:j+k])
            random.shuffle(kmer_ls) # WHY AM I SHUFFLING??? (if I'm just going to check if kmer is in other seqs)
            shuffled[header].append(kmer_ls) # maybe replace key with header
    score = score_seq(seqs, kmer_ls, k, comp)
    return score

def score_seq(seq_list, kmer_ls, comp, k=5):
    score = {kmer: [] for kmer in kmer_ls}
    for seq in seq_list:
        for kmer in kmer_ls:
            reverse = reverse_complement(kmer)
            observed = 1
            expected = 1
            observed_r = 1
            expected_r = 1
            # could i do:  observed = expected = observed_r = expected_r = 1
            for i, j in zip(kmer, reverse):
                expected *= comp[i]
                expected_r *= comp[j]
            observed = seq.count(kmer) / len(kmer_ls) 
            observed_r = seq.count(reverse) / len(kmer_ls)
            score_kmer = (math.log2(observed / expected) if observed != 0 else 0)
            score_reverse = (math.log2(observed_r / expected_r) if observed_r != 0 else 0)
            score[kmer] = [score_kmer, score_reverse]
    return score


introns = ortho_introns(args.filename, args.kmer, args.shuffles, args.composition)
print(introns)


# TO DO:
# []: Testing: how to double check answers?
# []: Check reverse strand


