for num in range(511, 10000):
    b = bin(num)[2:]
    count_1 = b[1::2].count('1')
    count_0 = b[0::2].count('0')
    if abs(count_1 - count_0) == 5:
        print(num)
        break