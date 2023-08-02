import numpy as np

def minimi_quadrati_pesati(x, y, errori):
    # Calcola i pesi come l'inverso quadrato degli errori
    pesi = 1 / errori**2
    
    # Costruisce la matrice di progettazione X
    X = np.vstack((np.ones_like(x), x)).T
    
    # Calcola i prodotti pesati
    X_pesati = np.sqrt(pesi)[:, np.newaxis] * X
    y_pesati = np.sqrt(pesi) * y
    
    # Calcola i coefficienti pesati
    coeff_pesati = np.linalg.lstsq(X_pesati, y_pesati, rcond=None)[0]
    
    # Calcola gli errori sui coefficienti
    residui_pesati = y_pesati - X_pesati.dot(coeff_pesati)
    scarti_quad_pesati = pesi * residui_pesati**2
    covarianza_pesata = np.linalg.inv(X_pesati.T.dot(X_pesati))
    err_coeff_pesati = np.sqrt(np.diagonal(covarianza_pesata) * np.sum(scarti_quad_pesati) / (len(x) - 2))
    
    return coeff_pesati, err_coeff_pesati

# Esempio di utilizzo
x = np.array([1, 2, 3, 4, 5])
y = np.array([1.2, 2.5, 3.6, 4.8, 5.9])
errori = np.array([0.1, 0.2, 0.1, 0.3, 0.2])

coeff, err_coeff = minimi_quadrati_pesati(x, y, errori)
print("Coefficienti:", coeff)
print("Errori sui coefficienti:", err_coeff)
