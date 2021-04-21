# Please make sure to check Indentation if code shows error
    n = int(input())
    a = []
    for x in range(n):
        a.append(input().split())
    query_name=input()

    #creating ditionary 
    testdic={}
    for x in range(0,len(a)):
        testdic[a[x][0]]=a[x][1:4]

#calculating average    
    ave=0
    for x in testdic[query_name]:
        ave+=float(x)

#finalizating output    
    ave=float(ave/len(testdic[query_name]))
    forave="{:.2f}".format(ave)

#printing output
    print(forave)

# Code credit :- Akshat Jain  
# HackerRank Link :- https://www.hackerrank.com/akshat_jjain?hr_r=1
