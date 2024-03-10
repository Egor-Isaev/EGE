import math
def divs_count(n):
    divs = set()
    for div in range(2, int(n ** 0.5) + 1):
        if n % div == 0:
            divs.add(div)
            divs.add(n // div)
    return sorted(divs)

for n in range(200000001,100000000000000):
    s = divs_count(n)
    if len(s) > 5:
        m = s[0]*s[1]*s[2]*s[3]*s[4]
        if m < n:
            print(m)