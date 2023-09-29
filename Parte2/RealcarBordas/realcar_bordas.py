import cv2

# ler imagem no formato BGR
imagem = cv2.imread("../../Imagens/imagem.png")

# Converter a imagem para escala de cinza
imagem_cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

# Aplicar um filtro de realce de bordas
imagem_realcada = cv2.Laplacian(imagem_cinza, cv2.CV_64F)

# armazenar imagem
cv2.imwrite("imagem_realcada.png",imagem_realcada)
