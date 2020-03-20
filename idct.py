from math import cos, pi, sqrt
import numpy as np

def def_idct2D(image):
    height = image.shape[0]
    width =  image.shape[1]

    dct_matrix_L = np.zeros_like(image).astype(float)
    dct_matrix_C = np.zeros_like(image).astype(float)

    for h in range(height):
        # IDCT na linhas
        dct_matrix_L[h, :] = idct_1d(image[h, :])
    for w in range(width):
        #  IDCT nas colunas
        dct_matrix_C[:, w] = idct_1d(dct_matrix_L[:, w])
    return dct_matrix_C

def idct_1d(image):

    n = len(image)
    idctImagem = np.zeros_like(image).astype(float)
    for i in range(n):
        soma = 0
        for k in range(n):
            ck = sqrt(0.5) if k == 0 else 1 # operador tenario para verificar o valor do CK
            soma += ck * image[k] * cos(2 * pi * k / (2.0 * n) * i + (k * pi) / (2.0 * n))

        idctImagem[i] = sqrt(2.0 / n) * soma

    return idctImagem
