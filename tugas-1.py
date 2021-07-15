import math

def qf(a, b, c) :
    print("quadratic function: f(x)=", end="")
    
    if a != 1 : print(a, end="")
    print("x^2", end="")
    
    if b>0 : print("+", end="")
    
    if b != 1 : print(b, end="")
    print("x", end="")
    
    if c>0 : print("+", end="")
    
    print(c)
    
def csf(a, b, c) :
    print("complete square form: f(x)=", end="")
    
    if a != 1 : print(a, end="")
    print("(x", end="")
    
    d = b/(2*a)
    
    if d>0 : print("+", end="")
    print(d, end="")
    print(")^2", end="")

    e = c - (b*b)/(4*a)
    
    if e>0 : print("+", end="")
    print(e)

def vertex(a, b, c) :
    print("vertex: (", end="")
    x = -b/(2*a)
    print(x, end="")
    print(",", end="")
    y = a*x*x + b*x + c
    print(y, end="")
    print(")")
    
def yintercept(a, b, c) :
    print("y-intercept: (0,", end="")
    print(c, end="")
    print(")")
    
def diskriminan(a, b, c) :
    d = b*b - 4*a*c
    print("discriminant value D=", end="")
    print(d)
    
def xintercept(a, b, c) :
    print("x-intercept: ", end="")
    d = b*b - 4*a*c
    
    if d<0 : print("none")
    else :
        print((-b+math.sqrt(d))/(2*a), end="")
        
        if d!=0 :
            print(" and ", end="")
            print((-b-math.sqrt(d))/(2*a))
        else :
            print("")

def solve(a, b, c) :
    qf(a, b, c)
    csf(a, b, c)
    print("")
    
    vertex(a, b, c)
    yintercept(a, b, c)
    diskriminan(a, b, c)
    xintercept(a, b, c)

solve(1, 4, 24)
print("")
solve(1, 4, -24)
