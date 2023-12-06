rows=5
for i in range(1,rows):
    for j in range(i):
        print("*",end="")
    for j in range(rows-i):
        print(" ",end="")
    print()    
