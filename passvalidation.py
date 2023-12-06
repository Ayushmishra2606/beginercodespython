#. Password Validation:
pswd="ayush2606"

while 1:
    user_pass=input("enter the pass")
    if user_pass==pswd:
        print("log in succesfull")
        break
    else:
        print("wrong password try again")
