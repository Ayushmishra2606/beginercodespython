# Guess the Number Game:
# Create a simple number guessing game where the computer selects a random number between 1
#and 100, and the user has to guess it. Use a while loop to keep the game running until the user
#guesses correctly

from random import *
name1=input("enter your name")
name2=input("enter your name")
num=randrange(1,101)
score=10
while 1:
     num2=int(input("guess the number"))
     if num==num2 :
         print("you won with score",score)
         if score%2==0:
         break
     elif num2>num:
         print("larger")
     else:
         print("smaller")
     score=score-1    



     
    
