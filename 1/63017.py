from itertools import permutations

graph = 'АБ АВ АГ АЖ ЖА ЖИ ЖЕ ЖГ ГА ГЖ ГЕ ЕГ ЕЖ ЕИ ЕД ИЕ ИЖ ИД ИБ ДЕ ДИ ДБ ДВ ВА ВД ВБ БА БВ БД БИ'
table = '13 14 16 23 24 27 28 31 32 34 38 41 42 43 46 56 57 58 61 64 65 67 72 75 76 78 82 83 85 87'
print('1 2 3 4 5 6 7 8')
for p in permutations('АБВГДЕИЖ'):
    new_t = table
    for i in range(1, 9):
        new_t = new_t.replace(str(i), p[i - 1])
        if set(new_t.split()) == set(graph.split()):
            print(' '.join(p))
