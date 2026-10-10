
def sum(li):
    sum=0
    for i in range(len(li)):
        sum = sum + li[i]
    return sum
li=[31,34,42,2,4,23]
print(sum(li))