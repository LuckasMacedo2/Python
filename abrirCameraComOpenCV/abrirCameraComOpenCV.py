from cv2 import cv2
import numpy as np


cv2.namedWindow("Previa")   # Cria uma janela para exibir imagens
cv = cv2.VideoCapture(0)    # Abre a câmera para a captura do vídeo

if cv.isOpened():           # Tentar capturar o primeiro frame
    rval, frame = cv.read()
else:
    rval = False

# Captura os vídeos em tempo real
while rval:
    cv2.imshow("preview", frame)    # Mostra o frane  
    rval, frame = cv.read()         # Lê o frame
    key = cv2.waitKey(20)           # Espera 20 segundos
    if key == 27:                   # ESC para sair
        break
cv2.destroyWindow("preview")