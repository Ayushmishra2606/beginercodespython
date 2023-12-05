#wap to display repeated character in a string
st=input('enter the string')
reg=''
for i in st:
    if i not in reg and st.count(i)>=2 :
        reg+=i
print(reg)
        
