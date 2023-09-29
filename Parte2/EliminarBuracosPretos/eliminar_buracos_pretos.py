import cv2

# ler a imagem

imagem = cv2.imread("../../Imagens/imagem.png")

# Converter a imagem para escala de cinza
imagem_cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

# Encontrar contornos dos objetos pretos
contornos, _ = cv2.findContours(imagem_cinza, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Eliminar objetos pretos
for contorno in contornos:
        cv2.drawContours(imagem, [contorno], -1, (0, 0, 0), thickness=cv2.FILLED)


# armazenar imagem 

cv2.imwrite("imagem_objetos_eliminados.png", imagem_cinza)

