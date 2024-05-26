for a in range(256):
    f = True
    for x in range(256):
        if not (((x & 45 > 0) or (x & 89 > 0)) <= (x & a > 0)):
            f = False
    if f:
        print(a)
