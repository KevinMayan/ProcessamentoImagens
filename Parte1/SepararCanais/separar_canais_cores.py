import cv2

# ler imagem em escala BGR

imagem = cv2.imread("../../Imagens/lena.png", cv2.IMREAD_COLOR)


# separar canais da imagem em escala BGR

canal_b, canal_g, canal_r = cv2.split(imagem)

# armazenar canais de cores


cv2.imwrite("canal_b.png", canal_b)

cv2.imwrite("canal_g.png", canal_g)

cv2.imwrite("canal_r.png", canal_r)
