import cv2
import imutils
import os

Datos = 'n'
Datos_resize = Datos + '_resize'
if not os.path.exists(Datos_resize):
    print("Carpeta creada: ", Datos_resize)
    os.mkdir(Datos_resize)
    
from_inicio = 0
from_final = 1870
to = 0

for i in range(from_inicio,from_final):
    try:
        objeto = cv2.imread(Datos+'/objeto_{}.jpg'.format(i))
        resized = imutils.resize(objeto, width=36) 
        cv2.imwrite(Datos_resize+'/objeto_{}.jpg'.format(to), resized)
        print(Datos_resize+'/objeto_{}.jpg'.format(to))
        to = to + 1
    except:
        print('Error en imagen ' + Datos + '/objeto_{}.jpg'.format(i))            
