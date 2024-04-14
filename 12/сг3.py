for a in range(1, 1000):
    for b in range(1, 1000):
        for c in range(1, 1000):
            s = '0' + a * '1' + b * '2' + c * '3' + '0'
            while not '00' in s:
                s = s.replace('011','201',1)
                s = s.replace('03', '220', 1)
                s = s.replace('02', '210', 1)
                s = s.replace('012', '2101', 1)
                s = s.replace('013', '12101', 1)
                s = s.replace('010', '1100', 1)
                if s.count('1') == 220 and s.count('2') == 197 and a+b+c == 198:
                    print(a,b,c)


