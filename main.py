# Importación de la libreria opencv
import cv2

# Lectura de las imagenes
imagen1 = cv2.imread("./yaktocat.png")
imagen2 = cv2.imread("./octocat-de-los-muertos.jpg")

img1 = cv2.resize(imagen1, (30, 30))
img2 = cv2.resize(imagen2, (30, 30))

# La cambia a blanco y negro
imagen_gris1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
imagen_gris2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

# Suma de las dos imagenes
resultado = imagen_gris1 + imagen_gris2

# Imprime el resultado de las imagenes sumadass
print(resultado)

# Mostramos la imagen
cv2.imshow("Imagenes combinadas", resultado)

# Guardamos la imagen 1
f = open("resultado_imagen1.txt", "w+")
f.write(str(imagen_gris1))

# Guardamos la imagen 2
f = open("resultado_imagen2.txt", "w+")
f.write(str(imagen_gris2))

# Guardamos la imagen 3
f = open("resultado_imagen.txt", "w+")
f.write(str(resultado))

# Indicamos que se tiene que esperar a que el usuario teclee el numero 0
# para el programa termine de ejecutarse
cv2.waitKey(0)
cv2.destroyAllWindows()