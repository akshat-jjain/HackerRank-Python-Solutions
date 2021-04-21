# Please make sure to check Indentation if code shows error
    n = int(input())
    a = 0
    arr = map(int, input().split())
    #for x in range(arr) :
    #    if a > x :
    #        a += x
    #        print(x) 
    #for y in range(a,0) :
    #    if arr.find(y) != -1 :
    #        print(y)
    #        break        
    arr1=list(arr)
    arr1.sort()
    arr1.reverse()
    y=arr1[0]
    for x in arr1:
        if x>=y:
            y=x
        else:
            print(x)
            break

# Code credit :- Akshat Jain  
# HackerRank Link :- https://www.hackerrank.com/akshat_jjain?hr_r=1
