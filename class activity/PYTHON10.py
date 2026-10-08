age=int(input("enter your age"))
id = "MSC001"


if(age>=18):
    user_id = input('enter your ID in CAPS')
    if(id == user_id):
        print("accessed")
    else:
        print("your id is incorrect")
else:
    print("you are not grater then 18")            