def is_leap(year):
    leap = False
    
    # Write your logic here
    if year % 4 == 0 :
        leap = True
        if year % 100 == 0 : 
            leap = False
            if year % 400 == 0 :
                leap = True
    else :
        leap = False
    return leap


# Code credit :- Akshat Jain  
# HackerRank Link :- https://www.hackerrank.com/akshat_jjain?hr_r=1
