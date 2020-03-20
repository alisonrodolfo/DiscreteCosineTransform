from math import cos, pi, sqrt
import numpy as np

def def_dct2D(image, num):

    height = image.shape[0]
    width = image.shape[1]
    dct_matrix_L = np.zeros_like(image).astype(float)
    dct_matrix_C = np.zeros_like(image).astype(float)

    for h in range(height):
        # DCT na linhas
        dct_matrix_L[h, :] = dct_1d(image[h, :], num)
    for w in range(width):
        #  DCT nas colunas
        dct_matrix_C[:, w] = dct_1d(dct_matrix_L[:, w], num)

    #dct_matrix_C[0 , 0] = 0
    return dct_matrix_C

def dct_1d(image, num):
    n = len(image)
    dctImage= np.zeros_like(image).astype(float)
    for k in range(n):
        soma = 0
        for i in range(n):
            soma += image[i] * cos(2 * pi * k / (2.0 * n) * i + (k * pi) / (2.0 * n))
        ck = sqrt(0.5) if k == 0 else 1
        dctImage[k] = sqrt(2.0 / n) * ck * soma

    # salvando os N maiores numeros e zerandos todos os outros
    if num > 0:
        dctImage.sort()
        for i in range(num, n):
            dctImage[i] = 0

    return dctImage
