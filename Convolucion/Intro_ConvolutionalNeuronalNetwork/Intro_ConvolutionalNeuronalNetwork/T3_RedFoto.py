import cv2
import os
import numpy as np
from keras.models import load_model

# Cargar el modelo de la red neuronal y sus pesos
modelo = './modelo/modelo.h5'
pesos = './modelo/pesos.h5'
cnn = load_model(modelo)
cnn.load_weights(pesos)

# Dimensiones de la imagen de entrada para la red neuronal
alto, largo = 500, 500

def predict(file):
    imagen_a_predecir = cv2.imread(file)
    imagen_a_predecir = cv2.resize(imagen_a_predecir, (largo, alto))
    imagen_a_predecir = np.expand_dims(imagen_a_predecir, axis=0)
    arreglo = cnn.predict(imagen_a_predecir)
    resultado = arreglo[0]
    respuesta = np.argmax(resultado)

    match respuesta:
        case 0:
            return 'Willy'
        case 1:
            return 'Cueto'
        case 2:
            return 'Lili'
        case _:
            return '----'

# Inicializar la cámara
cam = cv2.VideoCapture(0)

contFotos = 0

while True:
    result, image = cam.read()

    if result:
        cv2.imshow("Camara_Principal", image)
        res = cv2.waitKey(1)

        if res == ord("q"):
            cam.release()
            cv2.destroyWindow("Camara_Principal")
            break
        elif res == ord(" "):
            cv2.imwrite("foto_" + str(contFotos) + ".png", image)
            etiqueta_prediccion = predict("foto_" + str(contFotos) + ".png")
            print('Predicción:', etiqueta_prediccion)
            contFotos += 1
    else:
        print("No se detectó imagen. ¡Inténtalo de nuevo!")
        break
