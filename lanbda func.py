#lambda expression(a function without a function name)
'''
fun_name=lambda argv: return_expression

'''
'''
def Add(a,b):
    return a+b
Add=lambda a,b: a+b
out=Add(2,4)
print(out)
'''
c=int(input("enter temp in celcius"))
farenheit=lambda c: (c*1.8)+32

print(farenheit(c))
