def sum(n):
    a = 0
    while n > 0:
        a += n % 10
        n = n // 10
    return a


for n in range(987654321,2123456790):
    n1 = bin(n)[2:]
    n1+=str(sum(n)%2)
    n1+=str(sum(int(n1,2))%2)
    n1+=str(sum(int(n1,2))%2)
    r=int(n1,2)
    print(r//8-n//8)
