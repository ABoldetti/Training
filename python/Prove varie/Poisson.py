from sympy import *

def PoissonBrakets( f , g , q:list , p:list):
    eq = 0
    if len(q)== len(p):
        for i in range(len(q)):
            eq += diff(f,q[i])*diff(g,p[i])-diff(f,p[i])*diff(g,q[i])
    else: print("ERRORE")
    return simplify(eq)

def Dim(n:int):
    a = []
    b = []
    for i in range(1 , n+1):
        a.append(f"q{i}")
        b.append(f"p{i}")
    stringa = ' '.join( a )
    stringb = ' '.join( b )
    a = symbols(stringa)
    b = symbols(stringb)
    return a,b


if __name__ == '__main__' :
    f = 'q1' 
    g = 'p1-2*q2'
    n = 2
    q,p=Dim(n)
    print(PoissonBrakets(f,g,q,p))
