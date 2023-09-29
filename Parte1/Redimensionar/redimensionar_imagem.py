import cv2

# ler imagem utilizando escala bgr

imagem_bgr = cv2.imread("../../Imagens/lena.png", cv2.IMREAD_COLOR)

# redimensionar imagem

imagem_menor = cv2.resize(imagem_bgr, (80,80) , fx = 0.5, fy = 0.5, interpolation = cv2.INTER_AREA)

imagem_maior = cv2.resize(imagem_bgr, (300,300), fx = 0.5, fy = 0.5 , interpolation =  cv2.INTER_LINEAR)

# armazenar imagens redimensionadas

imagem_menor = cv2.imwrite("imagem_menor.png", imagem_menor)

imagem_maior = cv2.imwrite("imagem_maior.png", imagem_maior)
