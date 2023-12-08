name1 = input()
name2 = input()
ch1 = input()
ch2 = input()

if ch1=="Rock" and ch2=="Scissor":
    print(name1,"Win")
elif ch1=="Paper" and ch2=="Rock":
    print(name1,"Win")
elif ch1=="Scissor" and ch2=="Paper":
     print(name2,"Win")
else:
    print(name2,"Win")
