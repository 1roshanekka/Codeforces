#443A
l=[]
s = input()
n = s.lower()
for x in n:
    if x.isalpha():
        l.append(x)

a = set(l)

print(len(a))
