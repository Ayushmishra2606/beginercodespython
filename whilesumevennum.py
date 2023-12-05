#. Sum of Even Numbers:
num=int(input("enter the no"))
i=1
s=0


while i<=num:
    if i%2==0:    
       s=s+i
    i=i+1
print("sum of ",num,"even number is",s)    
