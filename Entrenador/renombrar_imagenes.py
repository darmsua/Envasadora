import cv2
import imutils
import os

Datos_P = 'p'
if not os.path.exists(Datos_P):
    print("Carpeta creada: ", Datos_P)
    os.mkdir(Datos_P)
    
from_inicio = 0
from_final = 193
to = 1871

for i in range(from_inicio,from_final):
    objeto = cv2.imread(Datos_P+'/objeto_{}.jpg'.format(i))
    cv2.imwrite(Datos_P+'/objeto_{}.jpg'.format(to), objeto)
    print(Datos_P+'/objeto_{}.jpg'.format(to))
    to = to + 1
                
cv2.destroyAllWindows()