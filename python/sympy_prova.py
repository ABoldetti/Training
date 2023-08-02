from sympy import *
import matplotlib.pyplot as plt

def insert( a: bool) -> list:
    ausy= 'a'
    vector = list()
    while ausy !='' :
        if a:
            ausy = input( 'Inserire le variabili nell equazione\t' )
        else:
            ausy = input( 'Inserire le costanti nell equazione\t' )
        vector.append( ausy )
    string = ' '.join( vector )
    vector = symbols( string )
    return vector


def propagazione_dell_errore(variables, formula, sigmas) -> str:
    exp = 0
    for i in range( len( variables ) ):
        exp += (diff( formula, variables[i]))**2 * sigmas[i]**2
    final=latex(simplify(sqrt(exp)))
    print (final)
    string = f"""${final}$"""
    return string

variables=list()
sigmas=list()
constants=list()
ausy = 'a'

variables = insert(True)
constants = insert(False)

#creation of sigmas
for ausy in variables:
    sigmas.append( f"""sigma_{ausy}""" )
sigmastring = ' '.join( sigmas )
sigmas = symbols( sigmastring )

while ausy != 'no':
    formula = input( 'Inserire formula per la propagazione dell errore per intero seguendo la sintassi di python\t' )
    string = propagazione_dell_errore (variables, formula, sigmas)
    plt.title(string)
    plt.show()
    ausy = input( 'Vuoi continuare inserendo un altra formula? (inserire no per terminare)')



