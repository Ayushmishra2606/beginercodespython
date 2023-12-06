#write a python program to count the frequency of each character in a string


st=input("enter the string")
reg=''
for i in st:
    if i not in reg:
        print(f'{i}:{st.count(i)}')
        reg += i
