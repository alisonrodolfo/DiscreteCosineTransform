
import math
import numpy as np
import cv2
class InvalidMatrixSizeError(Exception):
    pass


# Calculate the DCT Matrix for an M x M matrix
def get_dct_matrix(m):

    dct_matrix = np.empty((m, m))

    for p in range(m):
        for q in range(m):
            if p == 0:  # Case: First row
                dct_matrix[p, q] = 1/math.sqrt(m)
            else:  # Every other row
                dct_matrix[p, q] = (math.sqrt(2/m))*math.cos((math.pi*((2*q)+1)*p)/(2*m))
    dct_matrix[0 , 0] = 0
    return dct_matrix


# Input Matrix = A
# DCT Matrix = T
# Transpose of DCT Matrix  = T'
# Computes T * A * T' to calculate DCT of A
def dct(a):
    if len(a) == len(a[0]):
        t = get_dct_matrix(len(a))
        b = np.matmul(t, a)
        out = np.matmul(b, t.T)
    else:
        raise InvalidMatrixSizeError("Matrix must be a square matrix")
    return out



img1 = cv2.imread('lena.png')
img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
cv2.imshow('input', img1)
w,h = img1.shape

# make a 32bit float for doing the dct within
img2 = np.zeros((w,h), dtype=np.float32)
print(img1.shape, img2.shape)
img2 = img2+img1[:w, :h]



if __name__ == '__main__':
    print("Running DCT:")
    print("Output array: ")
    final = dct(img2)
    #print(final)
    cv2.imwrite('dct.png', final)

key = -1
while(key < 0):
    cv2.imshow("DCT", final)

    key = cv2.waitKey(1)
cv2.destroyAllWindows()