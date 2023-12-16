for a in range(64):
    f = True
    for x in range(64):
        if not(((x & 42 != 0) or (x & 13 != 0)) <= ((x & 30 == 0) <= (x & a != 0)):
            f = False
    if f:
        print(a)