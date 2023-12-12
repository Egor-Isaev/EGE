
for n in range(1, 100):
    a = bin(n)[2:]
    a += bin(n % 3)[2:].zfill(2)
    a += bin(int(a,2) % 5)[2:].zfill(3)
    r = int(a, 2)
    print(n,r,r//n)
