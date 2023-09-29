import cv2
import numpy as np

# carregar a imagem
imagem = cv2.imread("../../Imagens/margaridas.png", cv2.IMREAD_GRAYSCALE)

# definir o tamanho dos quadrados e as dimensões da imagem
tamanho_quadrado = 100
altura, largura = imagem.shape

# função para aplicar a binarização em um quadrado da imagem
def binarizar_quadrado(quadrado):
        _, binarizado = cv2.threshold(quadrado, 128, 255, cv2.THRESH_BINARY)
        return binarizado

# loop para particionar a imagem em quadrados e aplicar a binarização
for y in range(0, altura, tamanho_quadrado):
    for x in range(0, largura, tamanho_quadrado):
        quadrado = imagem[y:y+tamanho_quadrado, x:x+tamanho_quadrado]
        quadrado_binarizado = binarizar_quadrado(quadrado)
        imagem[y:y+tamanho_quadrado, x:x+tamanho_quadrado] = quadrado_binarizado

# armazenar imagem

cv2.imwrite("imagem_particionada_binarizada.png",imagem )


