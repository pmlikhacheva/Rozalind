with open("rosalind_revc.txt", "r") as f:
    seq = f.read()
seq = seq.replace("\n","")

DNA_ReverseComplement = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}
def reverse_complement(seq):
    return ''. join([DNA_ReverseComplement[nuc] for nuc in seq])[:: -1]
print(reverse_complement(seq))