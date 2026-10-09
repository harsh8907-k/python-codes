def is_fibonacci(n):
    a,b =0,1
    while b<n:
        a,b =b, a+b
        return b == n
print(is_fibonacci(13))
print(is_fibonacci(14))

