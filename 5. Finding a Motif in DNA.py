s = 'GATATATGCATATACTT'
t = 'ATAT'

def DNA_motif(s, t):
    res =[]
    for i in range(len(s)-len(t)-1):
        if s[i:len(t)+i] == t:
            res.append(i)
    return res
print(*DNA_motif(s, t))