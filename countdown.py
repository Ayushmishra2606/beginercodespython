 #Write a program that takes an integer input from the user and counts down from that number to 1
#using a while loop

from time import *
num=input()

n=10
print("start")
while n>=0:
   print(n)
   n-=1
   sleep(1) 
