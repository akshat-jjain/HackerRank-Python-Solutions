s1=input().split()
s2=input()
s3=s2.replace("x",s1[0],s2.count("x"))
n=eval(s3)
if n==int(s1[1]):
    print("True")

else:
    print("False")
