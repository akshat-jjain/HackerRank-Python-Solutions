# Please make sure to check Indentation if code shows error
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    arr=[]
    arr3=[]
    for a in range(0,x+1):
        for b in range(0,y+1):
            for c in range(0,z+1):
                arr1=[]    
                arr1.append(a)
                arr1.append(b)
                arr1.append(c)
                arr.append(arr1)

    for x in arr:
        i=0
        for y in x:
            i+=y

        if i != n:
            arr3.append(x)
        #else:
            #arr3.append("Not mentioned")
        
            
    #print(arr)

    print(arr3)

# Code credit :- Akshat Jain  
# HackerRank Link :- https://www.hackerrank.com/akshat_jjain?hr_r=1
