from sympy import *
import matplotlib.pyplot as plt

def insert( a: bool) -> list:
    ausy= 'a'
    vector = list()
    while ausy !='' :
        if a:
            ausy = str(input( 'Inserire le variabili nell equazione una alla volta, non inserire nulla per fermare il ciclo\t' ))
        else:
            ausy = input( 'Inserire le costanti nell equazione una alla volta, non inserire nulla per fermare il ciclo\t' )
        vector.append( ausy )
    string = ' '.join( vector )
    vector = symbols( string )
    return vector


def derivazione(variables, formula, sigmas) -> str:
    exp = 0
    for i in range( len( variables ) ):
        exp += (diff( formula, variables[i]))**2 * sigmas[i]**2
    final=latex(simplify(sqrt(exp)))
    print (final)
    string = f"""${final}$"""
    plt.title(string)
    plt.show()
    return string

def propagazione_errore () -> str:
    sigmas=list()

    variables = insert(1)

    #creation of sigmas
    for ausy in variables:
        sigmas.append( f"""sigma_{ausy}""" )
    sigmastring = ' '.join( sigmas )
    sigmas = symbols( sigmastring )

    formula = input( 'Inserire formula per la propagazione dell errore per intero seguendo la sintassi di python\t' )
    return derivazione (variables, formula, sigmas)

if __name__ == '__main__' :
    propagazione_errore()