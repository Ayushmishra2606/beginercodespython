def vote(age):
    if (age>=18):
        print('you can vote')

    elif (age<=18):
        print('you cannot vote ')
    else:
        print('please enter the age in correct format')
    pass
a=int(input('enter the age'))
print(vote(a))
