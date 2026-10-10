def greatest(a,b,c,d):
    max = a
    if(b>max):
        max = b
    if(c>max):
        max = c
    if(d>max):
        max = d
    return max
print(greatest(10,20,9,80))                