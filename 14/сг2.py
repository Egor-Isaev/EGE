for x in range(1, 40):
    for y in range(1, 40):
        b = 5 * 40 ** 8 + 7 * 40 ** 7 + x * 40 ** 6 + 6 * 40 ** 5 + 9 * 40 ** 4 + 2 * 40 ** 3 + y * 40 ** 2 + 40 + 9
        d = int((x * 40 + y) ** 0.5)
        if b % 39 == 0 and d ** 2 == x * 40 + y:
            print(x * 40 + y)
