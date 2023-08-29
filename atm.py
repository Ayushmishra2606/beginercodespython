amount=int(input("enter the amount"))
amount=amount-100
twok=amount//2000
amount=amount-twok*2000

fiveh=amount//500
amount=amount-fiveh*500

oneh=amount//100

print("number of two thousand notes",twok)
print("number of five hundred notes",fiveh)
print("number of one hundred notes",oneh+1)
