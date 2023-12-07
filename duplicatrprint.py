#wap to print duplicate string


st=input('enter the string')
reg=''
for i in st:
    if st.count(i) >=2 and i not in reg:
        reg +=i
print(reg)  
