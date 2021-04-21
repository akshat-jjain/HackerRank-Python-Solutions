def swap_case(s):
    z = ""
    for x in s :
        if x.isupper() :
            z += x.lower()
        elif x.islower() :
            z += x.upper()
        else :
            z += x
    return z

# Code credit :- Akshat Jain  
# HackerRank Link :- https://www.hackerrank.com/akshat_jjain?hr_r=1
