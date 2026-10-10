def cnt(n):
    count = 0
    while(n>0):
        count = count+1
        n = n//10
    return count

print(cnt(178469))        