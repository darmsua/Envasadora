from twisted.internet import reactor, protocol
from twisted.internet.threads import deferToThread
import cv2
import threading
import json

class WebcamCapture:
    def __init__(self):
        self.cap = cv2.VideoCapture(0)
        if not self.cap.isOpened():
            raise Exception("No se pudo abrir la webcam.")
        self.running = True
        self.current_frame = None
        self.lock = threading.Lock()

    def start_capturing(self):
        while self.running:
            ret, frame = self.cap.read()
            if ret:
                with self.lock:
                    self.current_frame = frame

    def stop_capturing(self):
        self.running = False
        self.cap.release()

    def get_current_frame(self):
        with self.lock:
            return self.current_frame

class ObjectDetectionProtocol(protocol.Protocol):
    def __init__(self, factory):
        self.factory = factory

    def dataReceived(self, data):
        data_str = data.decode('utf_8')
        
        try:
            json_data = json.loads(data_str)
            print('Recibido comando: ' + json_data.get('command'))
            if json_data['command'] == 'I':
                deferToThread(self.detectObject)
        except:
            print("Error al decodificar JSON")

    def detectObject(self):
        # tamaño del buffer de recepción del cliente TCP
        #   el bloque de datos de TIA Portal que envía la petición debe tener el mismo tamaño
        buffer_rcv_size = 30 
        cuboClassif = cv2.CascadeClassifier('cascade_cube.xml')

        frame = self.factory.webcam_capture.get_current_frame()
        if frame is not None:
            gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

            # Devuelve al PLC un objeto indeterminado si no se identifica el envase correctamente
            detected_objects = {"object": "indeterminado"}
            cubo = cuboClassif.detectMultiScale(gray, 
                                                scaleFactor = 1.22,
                                                minNeighbors = 800,
                                                minSize=(300,300))
                                               
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
                cv2.putText(frame,'Envase',(x,y-10),2,0.7,(0,0,255),2,cv2.LINE_AA)
                # Identificado un envase cúbico
                detected_objects = {"object": "cubo"}
            

            cv2.imshow('Inspector ML',frame)
            cv2.waitKey(1)  # Usamos un delay corto para permitir el procesamiento de la GUI
            
            # Convertir el resultado a una cadena JSON para enviar
            result_str = json.dumps(detected_objects, ensure_ascii=True)
            if len(result_str) < buffer_rcv_size:
                result_str_completo = result_str.ljust(buffer_rcv_size, ' ')
            # Enviar el resultado al cliente
            print('Inferencia: ' + result_str_completo)
            reactor.callFromThread(self.transport.write, result_str_completo.encode('utf-8'))

        else:
            detected_objects = {"object": "frame_None"}
            result_str = json.dumps(detected_objects, ensure_ascii=True)
            if len(result_str) < buffer_rcv_size:
                result_str_completo = result_str.ljust(buffer_rcv_size, ' ')
            
            print('Inferencia: ' + result_str_completo)
            reactor.callFromThread(self.transport.write, result_str_completo.encode('utf-8'))


class ObjectDetectionFactory(protocol.Factory):
    def __init__(self):
        self.webcam_capture = WebcamCapture()
        threading.Thread(target=self.webcam_capture.start_capturing).start()
        print("Inspector ML iniciado...")

    def buildProtocol(self, addr):
        return ObjectDetectionProtocol(self)

    def stopFactory(self):
        self.webcam_capture.stop_capturing()

if __name__ == '__main__':
    reactor.listenTCP(2000, ObjectDetectionFactory())
    reactor.run()



