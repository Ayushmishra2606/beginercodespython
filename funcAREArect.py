def area_of_rect(l,b):
    area=l*b
    return area
def peri(l,b):
    peri=2*(l+b)
    return peri
length=int(input('enter the length'))
breadth=int(input('enter the breadth'))
area=area_of_rect(length ,breadth)
peri=peri(length ,breadth)

print('area of the rect',area)
print('peri of the rect',peri)
