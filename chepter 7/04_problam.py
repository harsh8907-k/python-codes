m = int(input("enter a prime number"))

for i in range( 2, m):
    if(m%i) == 0:
        print("number is not prime")
    else:
        print("number is prime")