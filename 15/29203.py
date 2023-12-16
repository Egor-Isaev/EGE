for a in range(64):
    f = True
    for x in range(64):
        for y in range(64):
            if not ((3 * x + 7 * y < a) or (x >= y) or (y > 6)):
                f = False
    if f:
        print(a)
