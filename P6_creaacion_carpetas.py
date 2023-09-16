
import os
import shutil
from keras.utils import load_img, save_img, array_to_img, img_to_array

def get_folders_name_from(from_location, ignored_directories ):
    list_dir = os.listdir(from_location)
    folders = []
    for file in list_dir:
        temp = os.path.splitext(file)
        if temp[1] == "" and (temp not in ignored_directories):
            folders.append(temp[0])
    return folders

#kernel 1
def filtro1(imagen_a_convolucionar):
    return  imagen_a_convolucionar

base_location = "./"
source_folder = 'ImagenesPersonales'
destination_folder = 'CreaCarpetas'
ignored_directories = ['.idea', '.DS_Store'] #or other folders

name_folders = get_folders_name_from(base_location + source_folder, ignored_directories)  # custom location
#print(name_folders)

for folder in name_folders:
    try:
        ##read content - source location
        rutaImagen = base_location + source_folder + "/" + folder
        imgs = [archivo for archivo in os.listdir(rutaImagen) if archivo.endswith(".jpeg")]

        ##write content - destination location
        exists = os.path.exists(base_location + destination_folder + '/' + folder)
        if exists:
            shutil.rmtree(base_location + destination_folder + '/' + folder) #remove folder and subfolders

        #create a new folder...
        os.mkdir(base_location + destination_folder + '/' + folder)

        for k in range(5): #tot_kernels
            ruta = base_location + destination_folder + '/' + folder + "/Kernel_" + str(k)
            os.mkdir(ruta)
            for imagen in imgs:
                rutaImagenActual = rutaImagen + "/" + imagen
                img_a_procesar = load_img(rutaImagenActual, target_size=(500, 500), color_mode="grayscale")
                #######################################################################################################
                ##Aplica kernel "k" y guarda la imagen en ruta + nombre
                img_convolucionada = filtro1(img_a_procesar)  ## se debe cambiar....
                img = img_to_array(img_convolucionada)
                rutaToSave = ruta + "/" + imagen[0:imagen.index(".")] + "_conFiltro_" + str(k) + ".jpeg"
                save_img(rutaToSave, img)
                #######################################################################################################
                #######################################################################################################
                ##Aplica maxPooling al kernel "k" y guarda la imagen en ruta + nombre
                img_convolucionada = filtro1(img_a_procesar)  ## se debe cambiar....
                img = img_to_array(img_convolucionada)
                rutaToSave = ruta + "/" + imagen[0:imagen.index(".")] + "_conMaxPooling_" + str(k) + ".jpeg"
                save_img(rutaToSave, img)
                #######################################################################################################

    except Exception as ex:
        print('-----> ERROR!!!   ', ex)
    finally:
        pass








