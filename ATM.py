amount = int(input("Enter the amount : "))

amount = amount - 100

twok = amount//2000
amount = amount - (2000 * twok )

fiveh = amount//500 
amount = amount - (500 * fiveh )
oneh = amount//100 

print("Total number of two thousand notes : ",twok)
print("Total number of 5 hundred notes : ",fiveh)
print("Total number of one hundred notes : ",oneh+1)
