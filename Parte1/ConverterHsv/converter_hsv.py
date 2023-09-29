import cv2

# ler a imagem  em escala BGR

imagem = cv2.imread("../../Imagens/lena.png")

# converter imagem para HSV

imagem_hsv = cv2.cvtColor(imagem, cv2.COLOR_BGR2HSV)

# armazenar imagem

cv2.imwrite("lena_hsv.png", imagem_hsv)
