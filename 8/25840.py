import itertools

l = itertools.product('БЕЛКА', repeat=4)
cnt = 0
for str in l:
    line = ''.join(str)
    if line.count('Б')==1:
        cnt+=1
print(cnt)