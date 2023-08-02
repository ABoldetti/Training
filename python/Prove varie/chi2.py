import numpy as np
import scipy.stats as sp

def devstd (x : np.array):
    avg= np.mean(x)
    b=np.array([])
    for i in range (x):
        b[i]=x[i]-avg
        b[i]=b[i]**2
    return (np.sum(b)/len(x))

def chiq (x : np.array, y : np.array , sy : np.array):
    A,B=InterpolazioneLinearePesata (x,y,sy)
    chi=np.zeros(len(x))
    for i in range (len(x)):
        chi[i] = ((A*x[i]+B - y[i])/sy[i])**2
    ausy = np.sum(chi)
    if B/A <= 0.05 : dof = len (x)-1
    else : dof = len (x)-2
    print ("Il chi quadro con ", dof, "gradi di libertà, ha valore di", ausy, "con probabilità", sp.chi2(ausy, dof))
    

def InterpolazioneLinearePesata (x : np.array , y : np. array , sy : np.array):
    delta = np.sum (1/sy**2) * np.sum ((x/sy)**2) - (np.sum (x/sy))**2
    A = np.sum (y/(sy**2)) * np.sum ((x/sy)**2) - np.sum (x/(sy**2)) *np.sum(x*y/(sy**2))
    A /=delta
    B = np.sum (1/sy**2) * np.sum((x/sy)**2) - np.sum(x/(sy**2)) * np.sum (y/(sy**2))
    B /= delta
    sA = np.sqrt(np.sum((x/sy)**2)/delta)
    sB = np.sqrt( np.sum(1/sy**2)/delta)
    print("La retta interpolata ha equazione:\n", A, "+-", sA, "x +", B, "+-", sB)
    return A,B



X = np.array([1500,2000,3000,4000,4500,5000,6000])
Y = np.array([0.078,0.105,0.131,0.159,0.184,0.211,0.234])
sY = np.array([0.000323,0.000424,0.000346,0.000112,0.000320, 0.000363,0.000870])
# if input ("Deviazione singola?")=='s' :
#     sY=devstd(Y)
#     A,B=InterpolazioneLineare(X,Y,sY)
# else :
#     sY=([])
chiq(X,Y,sY)
