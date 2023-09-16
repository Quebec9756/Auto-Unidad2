from keras.utils import load_img, img_to_array, array_to_img, save_img #alternative 2

def getArrayImagen(nombre_archivo, largo = 500, alto = 500):
    img_original = load_img(nombre_archivo, target_size = (largo, alto),color_mode = "grayscale")
    img_en_arreglo = img_to_array(img_original)  # filas, columnas, canales de colores
    return img_en_arreglo

largo, alto = 500, 500

#file = './FIT V.jpg'
file = './gato.jpeg'

img_array = getArrayImagen(file, largo, alto)
print(img_array.shape)

stride = 3 # 2 x 2

img_max_pooling = []
for filas in range(1, alto - 1, stride):
    new_fila = []
    for columnas in range(1, largo - 1, stride):
        max_pixel = -1
        for f_kernel in range(stride):
            for c_kernel in range(stride):
                pixel = img_array[filas+f_kernel][columnas+c_kernel][0]
                if pixel > max_pixel:
                    max_pixel = pixel
        new_fila.append([max_pixel])  #se agrega como lista para agregarlo como canal 1 (escala de grises)
    img_max_pooling.append(new_fila)

img = array_to_img(img_max_pooling)
print(img.size)
img.show()
