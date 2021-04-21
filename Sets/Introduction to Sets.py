def average(array):
    # your code goes here
    y=0
    arr1=set(array)
    for x in arr1:
        y+=x
    z=y/len(arr1)    
    return z
