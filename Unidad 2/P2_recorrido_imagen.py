from keras.utils import load_img, img_to_array, array_to_img #alternative 2

largo, alto = 250,250
#file = './FIT V.jpg'
file = './gato.jpeg'

imagen_original = load_img(file, target_size = (largo, alto),color_mode = "grayscale")

arreglo_img_a_procesar = img_to_array(imagen_original)  #filas, columnas, canales de colores
print(arreglo_img_a_procesar.shape)


nombre_archivo  = 'en_pixeles_G.csv'
archivo_imagen = open(nombre_archivo, 'w')
#img_convolucionada = []
for filas in range(1,alto-1):
    #print("Fila:", filas + 1)
    #new_fila = []
    for columnas in range(1, largo-1):
        #print(columnas + 1, end= " ")
        pixel = str(arreglo_img_a_procesar[filas][columnas][0]) + ","
        print(pixel, end= "")
        archivo_imagen.write(pixel)
        #new_fila.append(arreglo_img_a_procesar[filas][columnas])
    #img_convolucionada.append(new_fila)
    archivo_imagen.write("\n")
    print()
archivo_imagen.flush()
archivo_imagen.close()

#img = array_to_img(img_convolucionada)
#print(img.size)
#img.show()


