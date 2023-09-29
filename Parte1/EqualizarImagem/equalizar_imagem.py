import cv2

# ler imagem em escala bgr

imagem = cv2.imread("../../Imagens/lena.png")

# converter  imagem BGR para GRAYSCALE

imagem_cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

# histograma da imagem em escala de cinza equalizada

imagem_cinza_equalizada = cv2.equalizeHist(imagem_cinza)

# armazenar imagem equalizada

cv2.imwrite("imagem_equalizada.png", imagem_cinza_equalizada)
