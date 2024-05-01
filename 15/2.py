for a in range(64):
    f = True
    for x in range(64):
        for b in range(24, 91):
            for c in range(47, 116):
                if not ((x in c) <= ((not (x in a) and (x in b))) <= not (x in c)):
                    f = False
    if f:
        print(a)
