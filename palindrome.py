# Palindrome Checker:

num=int(input("enter the number"))
s=0
cp=num

while num !=0:
    r=num%10
    s=s*10+r
    num=num//10

    if cp==s:
        print('palindrome number')
    else:
        print('not a palindrome number')
