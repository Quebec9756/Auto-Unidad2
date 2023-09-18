from keras.utils import load_img, img_to_array, array_to_img, save_img

def getArrayImagen(nombre_archivo, largo=500, alto=500):
    img_original = load_img(nombre_archivo, target_size=(largo, alto), color_mode="grayscale")
    img_en_arreglo = img_to_array(img_original)  # filas, columnas, canales de colores
    return img_en_arreglo

def convolucionar(img_a_convolucinar, kernel_type="sharpen", largo=500, alto=500):
    kernels = {
        "box": [
            [1, 1, 1],
            [1, 1, 1],
            [1, 1, 1]
        ]
        ,
        "ridge": [
            [0, -1, 0],
            [-1, 4, -1],
            [0, -1, 0]
        ],
        "edge": [
            [-1, -1, -1],
            [-1, 8, -1],
            [-1, -1, -1]
        ],
        "sharpen": [
            [0, -1, 0],
            [-1, 5, -1],
            [0, -1, 0]
        ],
        "gauss": [
            [1, 2, 1],
            [2, 4, 2],
            [1, 2, 1]
        ]
    }

    if kernel_type not in kernels:
        print("Kernel no válido")
        return None

    kernel = kernels[kernel_type]

    img_convolucionada = []
    for filas in range(1, alto - 1):
        new_fila = []
        for columnas in range(1, largo - 1):
            pixelConvulucionado = 0
            for f_kernel in range(len(kernel)):
                for c_kernel in range(len(kernel)):
                    pixelConvulucionado += kernel[f_kernel][c_kernel] * img_a_convolucinar[filas + (f_kernel - 1)][columnas + (c_kernel - 1)]
            if kernel == 'box':
                div = 9
            elif kernel == 'gauss':
                div = 16
            else:
                div = 1
            pixelConvulucionado = pixelConvulucionado / div
            new_fila.append(pixelConvulucionado)
        img_convolucionada.append(new_fila)
    img = array_to_img(img_convolucionada)
    return img

def plotImages(imgOriginal, imgConvolucionada):
    import matplotlib.pyplot as plt
    plt.figure(figsize=(15, 10))

    plt.subplot(1, 2, 1)
    plt.xticks([])
    plt.yticks([])
    plt.imshow(array_to_img(imgOriginal), cmap='gray')
    plt.title("Imagen Original")

    plt.subplot(1, 2, 2)
    plt.xticks([])
    plt.yticks([])
    plt.imshow(imgConvolucionada, cmap='gray')
    plt.title("Imagen Convolucionada")

    plt.show()

def applyAndSaveKernels(file):
    img_array = getArrayImagen(file)
    print(img_array.shape)

    kernel_types = ["box", "ridge", "edge", "sharpen", "gauss"]

    for kernel_type in kernel_types:
        img_conv = convolucionar(img_array, kernel_type)
        if img_conv is not None:
            print(f"Tamaño de la imagen convolucionada ({kernel_type}): {img_conv.size}")
            save_img(f'imagen_convolucionada_{kernel_type}.jpg', img_to_array(img_conv))
            plotImages(img_array, img_conv)


file = './gato.jpeg'
applyAndSaveKernels(file)
