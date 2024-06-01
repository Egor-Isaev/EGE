def convert(x2, x3):
    s = '0' + x3 * '3' + x2 * '2' + '0'
    while '00' not in s:
        s = s.replace('033', '1302', 1)
        s = s.replace('03', '120', 1)
        s = s.replace('023', '203', 1)
        s = s.replace('02', '20', 1)
    return s

for i in range(1, 20):
    s = convert(i, i)
    print(f"2:{i} 3:{i}\t1 - {s.count('1')}, 2 - {s.count('2')}, 3 - {s.count('3')}")
