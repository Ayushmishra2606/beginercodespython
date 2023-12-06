
def fact(a):
  s=1
  for i in range(1,a+1):
      s*=i
  return s;
dct={}
while 1:
    num=int(input('enter the number'))
    out=fact(num)
    print(f'factorial of the given number is {num}is {out}')
    dct[num]= out
    print('do you want to continue Y/N')
    if input() !='y':
        print(f'your all result{dct}')
        break
