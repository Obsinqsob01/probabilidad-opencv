# Importación de la libreria opencv
import cv2

import sys

# Lectura de argumentos para ver si el usuario esta mandando
# la ruta de las dos imagenes
if len(sys.argv) == 3:
    # Lectura de las imagenes
    imagen1 = cv2.imread(sys.argv[1])
    imagen1 = cv2.imread(sys.argv[2])

    # Suma de las dos imagenes
    resultado = imagen1 + imagen1

    # Mostramos la imagen
    cv2.imshow("Imagenes combinadas", resultado)

    # Indicamos que se tiene que esperar a que el usuario teclee el numero 0
    # para el programa termine de ejecutarse
    cv2.waitKey(0)