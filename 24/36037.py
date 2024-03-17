s = open('36037.txt').readline()
c = 0
if not 'XZZY' in s:
    c += s.count('X')+s.count('Y')+s.count('Z')
    