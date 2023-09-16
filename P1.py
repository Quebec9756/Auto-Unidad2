import matplotlib.pyplot as plt

from keras.utils import load_img, img_to_array

largo, alto = 500, 500

file = './ios13.jpg'

x = load_img(file, target_size=(largo, alto))

print(x.size)
print(x.mode)

# x.show()

plt.imshow(x)
plt.xticks()
plt.yticks()
plt.show()
