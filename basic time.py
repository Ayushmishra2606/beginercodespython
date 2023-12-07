sec=int(input("enter the time"))
h=sec//(60*60)
sec=sec%(60*60)
m=sec//60
sec=sec%60
print(f'{h}:{m}:{sec}')
