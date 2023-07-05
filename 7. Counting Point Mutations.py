s = 'GAGCCTACTAACGGGAT'
t = 'CATCGTAATGACGGCCT'
res = 0
for i in range(len(s)):
    if s[i]!=t[i]:
        res+=1
print(res)