# Máquina envasadora
Máquina de envasado con SIMATIC S7-1200

![Imagen de la maqueta](/info/1709402578558.jpg)

La estructura de la cinta transportadora está sacada de la web del CIFP Medina del campo, modificando la anchura del rodillo de la cinta para adecuarlo a un banda transportadora de 40 mm.

La reductora del motor también es originalmente del CIFP Medina del campo, con modificaciones para los soportes laterales de la caja. Los enlaces a la fuente original están archivos .txt dentro de la carpeta freeCAD.

El resto de accesorios de la cinta son originales, para el soporte de sensores, cámara, Ardunio Uno, servo, Raspberry Pi y encoder. 

Los laterales de la cinta transportadora están formados por tapas de canal protectora de 15 mm, aunque también se podrían imprimir. 

Estructura de directorios:

- info, incluye algunos archivos descriptivos de la máquina y videos de presentación de la misma.
- freeCAD, incluye todos los modelos necesarios para construir la cinta transportadora y el resto de accesorios.
    Están diseñados en FreCAD 0.21.1 y pueden modificarse fácilmente.
- stl, incluye todos los archivos en formato .stl para imprimirlos directamente.
- TIA portal, incluye el archivo de proyecto de TIA Portal V17.0
- Arduino, incluye el proyecto para Arduino UNO con una Ethernet Shield que contrala el servo del desviador de la cinta.
    El control se realiza desde el S7-1200 via Modbus TCP.
- Raspberry, incluye el programa Python para el inspector de objetos.
    El comando de inspección y la respuesta inferida por el modelo se envía al S7-1200 vía enlace TCP.
- Entrenador, incluye varios archivos Python para la captura de imágenes, cambio de resolución y el entrenamiento del 
    modelo de visión usando HAAR Cascade.


