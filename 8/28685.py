import itertools
l = itertools.product('ПЕТЯ', repeat = 6)
c = 0
for str in l:
    line = ''.join(str)
    if line.count('ПТ') == 0 and line.count('ТП') == 0 and line.count('ЕЯ') == 0 and line.count('ЯЕ') == 0 and line.count('ПП') == 0 and line.count('ТТ') == 0 and line.count('ЕЕ') == 0 and line.count('ЯЯ') == 0:
        c += 1
print(c)
