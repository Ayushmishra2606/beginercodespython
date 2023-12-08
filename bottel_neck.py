#important BOTTEL NECK PROBLEM

num = input("Enter the number : ").split()

ls = [int (i) for i in num]
reg = []

for i in ls:
    t=ls.count(i)
    reg.append(i)
print(t)