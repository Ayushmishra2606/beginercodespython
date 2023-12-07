#lambda with sorting
'''
ls=['abhiraj','zoya','manmohan','sakaham']
print('before sorting',ls)
ls.sort(key=lambda st:st[-1])
print('after sorting',ls)
'''


'''
ls=['abhiraj','zoya','manmohan','sakaham']
print('before sorting',ls)
ls.sort(key=lambda st: sum([ord(i) for i in st]))
print('after sorting',ls)
'''
#lambda with mapping
'''
ls=['abhiraj','zoya','manmohan','sakaham']
print('before sorting',ls)
out=list(map(lambda st: st.capitalize(),ls))
print('after sorting',out)
'''
'''
lst=[4,6,7,8]
print('before sorting',lst)
out=list(filter(lambda x: x<=5,lst))
print('after sorting',out)
'''
'''
def prime_or_not(num):
    for i in range(1,num):
        if i%2==0 :

lst=[4,6,7,8,19,15]
print('before sorting',lst)
out=list(filter(lambda x: for i in lst ,lst))
print('after sorting',out)
'''
