#  HP:(Hewlett-Packard) is a leading American multinational computer system manufacturer in the world.

#The company Hewlett-Packard doesn't like integers that are divisible by 3 or end with the digit 3 in their decimal representation. Integers that meet both conditions are disliked by Hewlett-Packard, too.

#Hewlett-Packard starts to write out the positive (greater than 0) integers which he likes: 1,2,4,5,7,8,10,11,14,16,….

#Write a program to print the output k-th element of this sequence (the elements are numbered from 1), where user will just enter the position only.

a = int(input())
count = 0

for i in range (1,1001):
    if i%3!=0 and i%10 !=3:
        count = count + 1
    if  count == a:
            print(i)
            break



















