import cv2
import numpy as np

# ler imagem na escala cinza

imagem = cv2.imread("../../Imagens/lena.png")


# converter imagem para escala de cinza

imagem_cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

# contruir histograma da imagem em escala de cinza

histograma = cv2.calcHist([imagem_cinza],[0],None,[256],[0,256])

# consturir histograma da imagem em escala BGR

histograma_azul = cv2.calcHist([imagem], [0], None, [256], [0,256])

histograma_verde = cv2.calcHist([imagem], [1], None, [256], [0,256])

histograma_vermelho = cv2.calcHist([imagem], [2], None, [256], [0,256])


# armazenar a imagem

cv2.imwrite("histograma_cinza.png", histograma)

cv2.imwrite("histograma_azul.png", histograma_azul)

cv2.imwrite("histograma_verde.png", histograma_verde)

cv2.imwrite("histograma_vermelho.png", histograma_vermelho)
