
from rembg import remove
from keras.utils import load_img, save_img

file = "gato.jpeg"
img = load_img(file, target_size = (500, 500))

img_new = remove(img) #remove bg ---create a RGBA image
#img_new.show()

#save_img("img_new.png", img_new) #save a RGBA IMAGE

img_converted = img_new.convert('RGB')
#img_converted.show()
#save_img("img_new.jpeg", img_converted)

##Downloading data from 'https://github.com/danielgatis/rembg/releases/download/v0.0.0/u2net.onnx' to file '/Users/alejandrohumbertogarciaruiz/.u2net/u2net.onnx'.