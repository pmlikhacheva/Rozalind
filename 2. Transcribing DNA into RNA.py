with open("rosalind_rna.txt", "r") as f:
    seq = f.read()
seq = seq.replace("\n","")

def transcription(seq):
    return seq.replace('T', 'U')

print(transcription(seq))