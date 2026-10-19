# Importamos las librerias
import cv2
import matplotlib.pyplot as plt

import os
ruta_imagen = os.path.join( 
    "img-original-0079",
    "Canguro-0079.jpg"
)

# Imagen
# Vamos a crear nuestra matriz principal
Canguro = cv2.imread(ruta_imagen)
# Corregimos
Canguro = cv2.cvtColor(Canguro, cv2.COLOR_BGR2RGB)
#print(Canguro) Muestra las matrices de la imagen
cv2.imshow("Canguro original 0079.jpg", Canguro)
cv2.waitKey(0) #Tiempo de espera
cv2.destroyAllWindows()#Destruye todas las ventanas