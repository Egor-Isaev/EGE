line = open('16388.txt').readline()
# KLMN
error_elements = ['KK', 'LL', 'MM', 'NN', 'LN', 'MK', 'KM', 'NL', 'NM', 'KN']

for elem in error_elements:
    while elem in line:
        line = line.replace(elem, f'{elem[0]} {elem[1]}')
print(len(max(line.split(), key=len)))
# 182