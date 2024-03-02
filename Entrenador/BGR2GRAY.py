import cv2
import imutils
import os

Datos = 'p'
Datos_GRAY = Datos + '_gray'
if not os.path.exists(Datos_GRAY):
    print("Carpeta creada: ", Datos_GRAY)
    os.mkdir(Datos_GRAY)
    
from_inicio = 0
from_final = 194
to = 0

for i in range(from_inicio,from_final):
    try:
        objeto = cv2.imread(Datos+'/objeto_{}.jpg'.format(i))
        gray = cv2.cvtColor(objeto,cv2.COLOR_BGR2GRAY)
        cv2.imwrite(Datos_GRAY+'/objeto_{}.jpg'.format(to), gray)
        print(Datos_GRAY+'/objeto_{}.jpg'.format(to))
        to = to + 1
    except:
        print('Error en imagen ' + Datos + '/objeto_{}.jpg'.format(i))            
