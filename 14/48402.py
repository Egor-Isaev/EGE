for x in range(0,10):
    b = int(f'3{x}DA',14) + int(f'5{x}A6',12)
    if b % 81 == 0:
        print(b // 81)



