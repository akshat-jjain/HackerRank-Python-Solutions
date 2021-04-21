#!/bin/python3

import math
import os
import random
import re
import sys



# Please make sure to check Indentation if code shows error
    n = int(input().strip())
    if n % 2 != 0 :
        print("Weird")
    elif n % 2 == 0 :
        if (n >= 2 and n <= 5) or (n > 20) :
            print ("Not Weird")
        else :
            print ("Weird")

# Code credit :- Akshat Jain  
#HackerRank Link :- https://www.hackerrank.com/akshat_jjain?hr_r=1
