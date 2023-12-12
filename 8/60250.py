import itertools

l = itertools.product('01234567', repeat=5)
c = 0
for str in l:
    line = ''.join(str)
    if line[0] != '0' and line.count('1') == 0 and line.count('35') == 0 and line.count('53') == 0 and line.count(
            '37') == 0 and line.count('73') == 0 and line.count('57') == 0 and line.count('75') == 0 and line.count(
        '24') == 0 and line.count('42') == 0 and line.count('46') == 0 and line.count('64') == 0 and line.count(
        '26') == 0 and line.count('62') == 0 and line.count('02') == 0 and line.count('20') == 0 and line.count(
        '40') == 0 and line.count('04') == 0 and line.count('60') == 0 and line.count('06') == 0 and line.count(
        '0') <= 1 and line.count('2') <= 1 and line.count('3') <= 1 and line.count('4') <= 1 and line.count(
        '5') <= 1 and line.count('6') <= 1 and line.count('7') <= 1:
        c += 1
print(c)
