def intersection(ar1,ar2):
    ls3=[i for i in arr1 if i in arr2]
    return ls3

def union(arr1,arr2):
    re=arr1+arr2
    reg=[]
    for i in arr1+arr2:
        if i not in reg:
            reg.append(i)
    return reg

def symmetric_difference(arr1,arr2):
    un=union(arr1,arr2)
    inte=interaction(arr1,arr2)
    for i in inte:
        un.remove(i)
    return un

ls1=[1,3,6]
ls2=[3,8,9,1]
re1= intersection(ls1,ls2)
print(re1)

re2=union(ls1,ls2)
print(re2)

re3=symmetric_difference(ls1,ls2)
print(re3)
