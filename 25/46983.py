def divs_count(n):
    divs = set()
    for div in range(2, int(n ** 0.5) + 1):
        if n % div == 0:
            divs.add(div)
            divs.add(n // div)
    if len(divs) >= 5:
        return sorted(list(divs))[4]
    else:
        return 0


for n in range(460000001, 460000010):
    a = divs_count(n)
    if a > 0:
        print(a)
