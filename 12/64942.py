for a in range(1, 400):
    for b in range(1, 510):
        s = '0' + b * '3' + a * '2' + '0'
        while '00' not in s:
            s = s.replace('033', '1302', 1)
            s = s.replace('03', '120', 1)
            s = s.replace('023', '203', 1)
            s = s.replace('02', '20', 1)
        if s.count('1') == 340 and s.count('2') == 849 and s.count('3') == 151:
            print(a)
