# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
strarr=[]

for x in range(n):
    strin=input()
    strarr.append(strin)

stradd=set(strarr)
print(len(stradd))
