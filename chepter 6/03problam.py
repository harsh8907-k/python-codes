marks1=int(input("Enter a marks: "))
marks2=int(input("Enter a marks: "))
marks3=int(input("Enter a marks: "))

total=100*marks1+marks2+marks3/300
if(total>=40):
    print("pass",total)
elif(total<=33):
    print("fail",total)    
else:   
    print("fail",total)
    