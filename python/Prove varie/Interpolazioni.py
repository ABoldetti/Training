import numpy as np

def InterpolazioneLineareOrigine(x,y,sy):
    '''
    Dati due vettori di pari dimensione x, y e l'incertezza sy si può interpolare la retta passante per l'origine con il metodo dei minimi quadrati
    '''
    # controllo che x e y abbiano pari dimensione diversa da 0
    if len(x) != len(y) or len(x) == 0:
        print('I dati inseriti non sono validi')
        return 0
    if sy ==0 :
        print("L'incertezza non può essere 0")
        return 0
    # calcolo le sommatorie
    sumxy = 0
    sumx2 = 0
    for i in range(len(x)): # range(n) = [0,1,2,..,n-1]
        sumxy += x[i]*y[i]
        sumx2 += x[i]*x[i]
    k = sumxy/sumx2
    sk = (float)(sy)/np.sqrt(sumx2)
    return (k,sk)

def InterpolazioneLineare(x,y,sy):
    if len(x) != len(y) or len(x) == 0:
        print('I dati inseriti non sono validi')
        return 0
    if sy ==0 :
        print("L'incertezza non può essere 0")
        return 0
    sumxy = 0
    sumx2 = 0
    sumy=0
    sumx=0
    for i in range(len(x)):
        sumy +=y[i]
        sumx+=x[i]
        sumxy += x[i]*y[i]
        sumx2 += x[i]*x[i]
    delta=(len(x)*sumx2)-(sumx**2)
    A=((sumy*sumx2)-(sumx*sumxy))/delta
    B=((len(x)*sumxy)-(sumx*sumy))/delta
    sA=(float)(np.sqrt(sumx2/delta))*(float)(sy)
    sB=(float)(np.sqrt(len(x)/delta))*(float)(sy)
    return(A,B,sA,sB)



