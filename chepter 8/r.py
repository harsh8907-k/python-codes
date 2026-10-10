def factorial(n):
    if(n==1 or n==0):
        return 1
    return n * factorial(n-1)

n = int(input("enter the number"))    
print(f"the factoial of the number is {factorial(n)}")