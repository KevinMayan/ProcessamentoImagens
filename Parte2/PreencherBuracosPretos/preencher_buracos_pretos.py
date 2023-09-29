import cv2

imagem = cv2.imread("../../Imagens/imagem.png")

# Converter a imagem para tons de cinza
imagem_cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

# Encontrar contornos dos objetos pretos
contornos, _ = cv2.findContours(imagem_cinza, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Preencher os objetos pretos
for contorno in contornos:
        cv2.drawContours(imagem, [contorno], -1, (255, 255, 255), thickness=cv2.FILLED)


cv2.imwrite("imagem_preenchida.png", imagem_cinza)
