#importações de biblioteca
import cv2
import numpy as np
#leitura da imagem
image = cv2.imread("image.png")
kernel = np.ones((6,6),np.float32)/25
filter2D = cv2.filter2D(image,-1,kernel)
#Fonte de texto
font = cv2.FONT_ITALIC
cv2.putText(image,'Original Image',(5,100), font, 1, (0,0,255), 2, cv2.LINE_4)
cv2.putText(filter2D,'Filter 2D',(45,100), font, 1, (0,0,255), 2, cv2.LINE_4)
#Salva imagens
cv2.imwrite("image.png", image)
cv2.imwrite("edit.png",filter2D)
cv2.imshow("Final Image",image)
#Exibir imagem
cv2.imshow("Final Image 1",filter2D)
cv2.waitKey(0)
