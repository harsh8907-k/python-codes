n=int(input("enter the star"))
for i in range(1,n + 1):
 print(" "* (n-1),end="")
 print("*"*(2*i-1),end="")
 print("")