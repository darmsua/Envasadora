import cv2
import numpy as np 
import imutils
import os

Datos_P = 'p'
if not os.path.exists(Datos_P):
    print("Carpeta creada: ", Datos_P)
    os.mkdir(Datos_P)
    
Datos_N = 'n'
if not os.path.exists(Datos_N):
    print("Carpeta creada: ", Datos_N)
    os.mkdir(Datos_N)


cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

x1, y1 = 20,20
x2, y2 = 450,450

count_P = 194
count_N = 1871

while True:
    
    ret, frame = cap.read()
    if ret == False: 
        print('Error al capturar imagen')
        break
    
    imAux = frame.copy()
    cv2.rectangle(frame, (x1,y1), (x2,y2), (255,0,0), 1)
    
    objeto = imAux[y1:y2, x1:x2]
    objeto = imutils.resize(objeto, width=76) 
    
    cv2.imshow('frame', frame)
    
    key = cv2.waitKey(1)
    if key == 27:
        break
        
    if key == ord('s'):
        gray = cv2.cvtColor(objeto,cv2.COLOR_BGR2GRAY)
        cv2.imwrite(Datos_P+'/objeto_{}.jpg'.format(count_P), gray)
        print('Imagen positiva guardada: ', 'objeto_{}.jpg'.format(count_P))
        count_P = count_P + 1
    
    if key == ord('n'):
        gray = cv2.cvtColor(objeto,cv2.COLOR_BGR2GRAY)
        cv2.imwrite(Datos_N+'/objeto_{}.jpg'.format(count_N), gray)
        print('Imagen negativa guardada: ', 'objeto_{}.jpg'.format(count_N))
        count_N = count_N + 1
        
cap.release()
cv2.destroyAllWindows()