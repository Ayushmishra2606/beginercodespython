a , b = input().split()
a = int(a)
b = int(b)
k = int(input())

re1 = a & b
re2 = a | b
re3 = a ^ b

if re1>=k:
    re1 = 0
if re2>=k:
    re2 = 0
if re3>=k:
    re3 = 0
m = max (re1,re2,re3)
print(m)

