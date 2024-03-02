import cv2
import numpy as np

def scalar(x_min, x_max, y_min, y_max, value):
    return y_min + (((y_max-y_min)/(x_max-x_min))*value)

def nothing1(val):
    pass

def nothing2(val):
    pass

def nothing3(val):
    pass

cv2.namedWindow('Clasificador')
cv2.createTrackbar('scale', 'Clasificador',0,1000,nothing1)
cv2.createTrackbar('neighborns', 'Clasificador',0,1000,nothing2)
cv2.createTrackbar('minSize', 'Clasificador',0,1000,nothing3)
cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)


cuboClassif = cv2.CascadeClassifier('cascade_cube.xml')
#cilindroClassif = cv2.CascadeClassifier('cascade_cilindro.xml')

while True:

    ret,frame = cap.read()
    if (ret == True):
        scale = scalar(0, 1000, 1.05, 5, 1 + cv2.getTrackbarPos('scale','Clasificador'))
        neighborns = 10 + cv2.getTrackbarPos('neighborns','Clasificador')
        size_x = 200 + cv2.getTrackbarPos('minSize','Clasificador')
        size_y = size_x
        print('scale: ', scale, ' neighborns: ', neighborns, ' minSize: ', size_x)
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        cubo = cuboClassif.detectMultiScale(gray, 
                                            scaleFactor = scale, #1.22
                                            minNeighbors = neighborns, #800
                                            minSize=(size_x,size_y))
                                                #maxSize=(300,300))
    
        for (x,y,w,h) in cubo:
            roi_gray = gray[y:y+h, x:x+w]
            # Aplicar detección de bordes de Canny a la ROI
            edges = cv2.Canny(roi_gray, 20, 70)

            # Encontrar contornos en la ROI después de la detección de bordes
            contours, _ = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

            # Dibujar los contornos encontrados
            for contour in contours:
                # Calcular los puntos para dibujar el contorno en la imagen original
                contour[:, :, 0] += x  # Desplazar en x
                contour[:, :, 1] += y  # Desplazar en y
                cv2.drawContours(frame, contour, -1, (0, 255, 0), 2)
            
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)
            cv2.putText(frame,'Cubo',(x,y-10),2,0.7,(0,0,255),2,cv2.LINE_AA)

        cv2.imshow('frame',frame)

    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()
    