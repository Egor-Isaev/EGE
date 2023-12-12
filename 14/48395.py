for x in range(0,10):
    b = int(f'28{x}2',18) + int(f'93{x}5',12)
    if b % 133 ==0:
        print(b//133)