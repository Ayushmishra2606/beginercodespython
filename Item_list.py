ls = []

while 1:
    item = input("Enter Item name : ")
    if item == "":
        break
    ls.append(item)

ls.sort()
print(ls)