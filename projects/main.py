pasword=123456
i=0
while i<3:
    paswordcheking=int(input("write pasword: "))
    if paswordcheking== pasword:
        print("you registrated succesfully!")
        break
    else:
        print("try again")
    i+=1
if i==3:
    print("maybe it's not your acount") 