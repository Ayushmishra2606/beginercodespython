'''
wap to prompt a user to read the marks of five different subject. cal the marks total marks and pecentage of the marks and display the grade according to the percentage
'''
sub1=eval(input( 'enter the marks of maths'))
sub2=eval(input('enter the marks of physics'))
sub3=eval(input('enter the marks of english'))
sub4=eval(input('enter the marks of web tech'))
sub5=eval(input('enter the marks of iot'))
tm=sub1+sub2+sub3+sub4+sub5
percent=tm/150*100
print('total marks=',tm)
print('percentage obtained',percent)

if percent>=90:
    print('distinction')

elif percent>=80:
    print('first class')

elif percent>=70:
    print('second class')

elif percent>=60:
    print('pass')

else:
    print("fail")

    
