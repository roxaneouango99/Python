##finding the roots of a function between a specific region
import math
def f(x):
    return 2*x + 1

def find_root(a, b):
    c = (a+b)/2
    ans = f(c)
    while ans != 0:
        c = (a+b)/2
        ans = f(c)
        if (ans > 0):
             c = b
             
        elif (ans < 0):
            c = a
        else:
            return c   

lower = -5
upper = 0
print(find_root(lower, upper))