# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
num =[]
bh = ["9","8","7"]
for x in range(0,n) :
    num.append(input())
for y in num :
    if len(y) == 10 and y[0] in bh and y.isdigit():
        print("YES")
    else :
        print("NO")
