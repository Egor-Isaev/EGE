for a in range(1, 100):
    for b in range(1, 100):
        for c in range(1, 100):
            s = '0' + a * '1' + b * '2' + c * '3'
            while '01' in s or '02' in s or '03' in s:
                s = s.replace('01', '30', 1)
                s = s.replace('02', '101', 1)
                s = s.replace('03', '202', 1)
            if s.count('1') ==  15 and s.count('2') == 10 and s.count('3') == 60:
                print(a)