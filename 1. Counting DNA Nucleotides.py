with open("rosalind_dna.txt", "r") as f:
    seq = f.read()
seq = seq.replace("\n","")
nucleotides_Counter = {'A':0, 'T':0, 'G':0, 'C':0}
for nuq in seq:
    nucleotides_Counter[nuq] += 1
print(*nucleotides_Counter.values())
