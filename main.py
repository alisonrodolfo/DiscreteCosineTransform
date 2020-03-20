import cv2
from DCT import dct
from DCT import idct

def main():
    img = cv2.imread("lena.jpg")
    numCoeficientes = 32
    print("Coeficiente de corte	" + str(numCoeficientes) + " !" + "\n")

    print("Executando DCT")
    imgResult = dct.def_dct2D(img, numCoeficientes)
    print("\nConcluido")
    cv2.imwrite('dct.jpg', imgResult)

    print("Executando DCT Inversa")
    idct_img = idct.def_idct2D(imgResult)
    print("\nConcluido")
    cv2.imwrite('idct.jpg', idct_img)


if __name__ == '__main__':
    main()
