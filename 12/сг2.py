m = 0
for a in range(1, 100):
    for b in range(1, 100):
        for c in range(1, 100):
            s = '0' + a * '1' + b * '2' + c * '3' + '0'
            while '00' not in s:
                s = s.replace('01', '220', 1)
                s = s.replace('02', '1013', 1)
                s = s.replace('03', '120', 1)
            if s.count('1') == 13 and s.count('2') == 18:
                print(a + b + c + 2)
