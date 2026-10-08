python=int(input("enter the marks:----------"))
java=int(input("enter the marks:---------"))
ml=int(input("enter the marks:--------"))
avg=(python+java+ml/3)
print(avg)
if(python<35 or java<35 or ml<35):
    print("you failed in one of the subject")
elif(avg>90):
    print("grade is A")
elif(avg>80):
    print('grade is B')
elif(avg>70):
    print('grade is C')
elif(avg>60):
    print('grade is D')
elif(avg>50):
    print('grade is E') 
elif(avg<35):
    print("you faild you are so dumb you have to suside")               
else:
    print("fail")        
