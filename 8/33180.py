import itertools

l=itertools.product('ТИМОФЕЙ', repeat=5)
c=0
for str in l:
    line= ''.join(str)
    if line.count('Й')<=1 and line.count('ЙИ')==0 and line.count('ИЙ')==0 and line[0]!='Й' and line[4]!='Й':
        c+=1
print(c)