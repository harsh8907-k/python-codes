a = int(input("enter the number"))
b = int(input("enter the number"))
c = int(input("enter the number"))
def gratest(a,b,c):
    if(a>b):
        print("a is gratest")
    elif(a>c):
        print("a is gratest")
    elif(b>c):
        print("b is gratest")
    elif(b>a):
        print("b is gratest")   
    elif(c>b):
        print("c is gratest")        
    elif(c>a):
        print("c is gratest")
print(gratest(a,b,c))        


        
        
