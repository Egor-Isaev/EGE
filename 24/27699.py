l = open('27699.txt').readline()
error = ['LL', 'LR', 'DL', 'DD', 'RR', 'RD']
for elem in error:
    while elem in l:
        l = l.replace(elem, f'{elem[0]} {elem[1]}')
print(len(max(l.split(), key=len)))