
for n in range(2, 10000):
    sum0 = 0
    sum1 = 0
    b = bin(n)[2:]
    for i in range(len(b)):
        if i % 2 == 0 and b[i] == '0':
            sum0 += 1
        elif i % 2 != 0 and b[i] == '1':
            sum1 += 1
        if abs(sum1 - sum0) == 4:
            print(n)

