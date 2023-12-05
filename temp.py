#input section
c=float(input("enter tenpreture in celcius"))
temp=input("farenheit or kelvin")

farenheit=(9/5*c)+32
kelvin=273.15 + c

if (temp==farenheit):
    print("temp=",farenheit)

else:
    print("temp=",kelvin)

    
