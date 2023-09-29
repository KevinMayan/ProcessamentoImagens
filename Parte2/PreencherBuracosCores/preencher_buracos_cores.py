import cv2
import numpy as np

imagem = cv2.imread("../../Imagens/imagem.png")

# Converter a imagem para o espaço de cores HSV
imagem_hsv = cv2.cvtColor(imagem, cv2.COLOR_BGR2HSV)

# Definir intervalos de cores para azul, amarelo e verde
azul_lower = np.array([90, 50, 50])
azul_upper = np.array([130, 255, 255])
amarelo_lower = np.array([20, 100, 100])
amarelo_upper = np.array([30, 255, 255])
verde_lower = np.array([35, 100, 100])
verde_upper = np.array([85, 255, 255])

# Criar máscaras para cada cor
mask_azul = cv2.inRange(imagem_hsv, azul_lower, azul_upper)
mask_amarelo = cv2.inRange(imagem_hsv, amarelo_lower, amarelo_upper)
mask_verde = cv2.inRange(imagem_hsv, verde_lower, verde_upper)

# Preencher os buracos dos objetos nas máscaras
mask_azul = cv2.morphologyEx(mask_azul, cv2.MORPH_CLOSE, np.ones((5, 5), np.uint8))
mask_amarelo = cv2.morphologyEx(mask_amarelo, cv2.MORPH_CLOSE, np.ones((5, 5), np.uint8))
mask_verde = cv2.morphologyEx(mask_verde, cv2.MORPH_CLOSE, np.ones((5, 5), np.uint8))



# armazenar imagem

cv2.imwrite("imagem_preenchida.png", imagem_hsv)
