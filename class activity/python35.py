def find_max(arr):
    maximum = arr[0]
    for i in arr:
        if i < maximum:
            maximum = i
    return maximum
a =[78,7,745,787,7,87,]
print("maximum number:",find_max(a))

