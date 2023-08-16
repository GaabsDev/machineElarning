import cv2

# Carregar a imagem colorida
imagem_colorida = cv2.imread('caminho_da_imagem.jpg')

# Converter a imagem para tons de cinza
imagem_cinza = cv2.cvtColor(imagem_colorida, cv2.COLOR_BGR2GRAY)

# Aplicar a binarização (limiar de 128)
limiar, imagem_binarizada = cv2.threshold(imagem_cinza, 128, 255, cv2.THRESH_BINARY)

# Salvar a imagem binarizada
cv2.imwrite('imagem_binarizada.jpg', imagem_binarizada)

# Mostrar as imagens
cv2.imshow('Imagem Colorida', imagem_colorida)
cv2.imshow('Imagem em Tons de Cinza', imagem_cinza)
cv2.imshow('Imagem Binarizada', imagem_binarizada)
cv2.waitKey(0)
cv2.destroyAllWindows()
