# Complete the solve function below.
def solve(s):
    y = ""
    spl = s.split(' ')
    for x in spl :
        #s = s.replace(x, x.capitalize())
        y+=x.capitalize()
        y+=" "
    return y.rstrip(" ")
