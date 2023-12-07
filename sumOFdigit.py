#wap to find the sum of the digit of the given number

num=eval(input(' enter the number'))
x=num
rem=0
sum=0

while num>0:
    rem=num%10
    num=num//10
    sum=sum+rem
print('sum of digits of',x,'is',sum)    

