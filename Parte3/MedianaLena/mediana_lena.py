import cv2

# ler imagem em escala BGR
imagem = cv2.imread("../../Imagens/lena.png")

# aplicar um filtro de mediana
imagem_mediana = cv2.medianBlur(imagem, 5)

# armazenar imagem

cv2.imwrite("imagem_mediana.png", imagem_mediana)
