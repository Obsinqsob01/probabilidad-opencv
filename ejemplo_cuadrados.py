# Importación de la libreria opencv
import cv2

# Lectura de las imagenes
imagen1 = cv2.imread("./cuadrado_azul.png")
imagen2 = cv2.imread("./cuadrado_rojo.png")

# Suma de las dos imagenes
resultado = imagen1 + imagen2

# Mostramos la imagen
cv2.imshow("Colores combinados", resultado)

# Indicamos que se tiene que esperar a que el usuario teclee el numero 0
# para el programa termine de ejecutarse
cv2.waitKey(0)
