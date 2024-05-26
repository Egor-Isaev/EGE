from collections import Counter

l = open('33526.txt').readline()
s = []
alp = 'QWERTYUIOPASDFGHJKLZXCVBNM'
for i in range(1, len(l) - 1):
    if l[i - 1] == l[i + 1]:
        s += str(l[i])
for c in alp:
    print(c, s.count(c))

