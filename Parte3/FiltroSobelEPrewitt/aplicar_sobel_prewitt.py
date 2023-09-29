import cv2
import numpy as np

# ler a imagem

imagem = cv2.imread('../../Imagens/coins.png')


# converter para escala de cinza

imagem_cinza = cv2.cvtColor(imagem,cv2.COLOR_BGR2GRAY)


# aplicar o filtro Sobel para detecção de bordas nas direções x, y e xy
sobel_x = cv2.Sobel(imagem_cinza, cv2.CV_64F, 1, 0, ksize=5)
sobel_y = cv2.Sobel(imagem_cinza, cv2.CV_64F, 0, 1, ksize=5)
sobel_xy = cv2.Sobel(imagem_cinza, cv2.CV_64F,1,1,ksize=5)

# definir o kernel do filtro Prewitt para detecção de bordas nas direções x e y
kernel_x = np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]], dtype=np.float32)
kernel_y = np.array([[-1, -1, -1], [0, 0, 0], [1, 1, 1]], dtype=np.float32)

# aplicar o filtro Prewitt nas direções x e y
prewitt_x = cv2.filter2D(imagem, -1, kernel_x)
prewitt_y = cv2.filter2D(imagem, -1, kernel_y)

# armazenar imagens
cv2.imwrite("sobel_x.png", sobel_x)
cv2.imwrite("sobel_y.png", sobel_y)
cv2.imwrite("sobel_xy.png", sobel_xy)
cv2.imwrite("prewitt_x.png", prewitt_x)
cv2.imwrite("prewitt_y.png", prewitt_y)
