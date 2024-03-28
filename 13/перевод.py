ip = '217.8.244.3'
print(' '.join([bin(int(o))[2:].zfill(8) for o in ip.split('.')]))
ip = '255.255.252.0'
print(' '.join([bin(int(o))[2:].zfill(8) for o in ip.split('.')]))