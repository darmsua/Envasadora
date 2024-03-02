# envasadora
Máquina de envasado con SIMATIC S7-1200

Estrucutra de directorios:

- info, incluye algunos archivos descriptivos de la máquina y videos de presentación de la misma.
- freeCAD, incluye todos los modelos necesarios para construir la cinta transportadora y el resto de accesorios.
    Están diseñados en FreCAD 0.21.1 y pueden modificarse fácilmente.
- stl, incluye todos los archivos en formato .stl para imprimirlos directamente. Se utilizó un perfil de impresora     
    Artillery Genius.
- TIA portal, incluye el archivo de proyecto de TIA Portal V17.0
- Arduino, incluye el proyecto para Arduino UNO con una Ethernet Shield que contrala el servo del desviador de la cinta.
    El control se realiza desde el S7-1200 via Modbus TCP.
- Raspberry, incluye el programa Python para el inspector de objetos.
    El comando de inspección y la respuesta inferida por el modelo se envía al S7-1200 vía enlace TCP.
- Entrenador, incluye varios archivos Python para la captura de imágenes, cambio de resolución y el entrenamiento del 
    modelo de visión usando HAAR Cascade.


