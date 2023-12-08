n = int(input())
w = len(bin(n)) -2
for i in range(n+1):
    x = bin(i)[2:]
    print(f'{x:>{w}}')
