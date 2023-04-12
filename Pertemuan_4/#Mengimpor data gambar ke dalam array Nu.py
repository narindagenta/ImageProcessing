#Mengimpor data gambar ke dalam array Numpy

import matplotlib.pyplot as plt 
import matplotlib.image as mpimg

from PIL import Image

img = mpimg.imread('kucing.jpg')
lum_img = img[:, :, 0]

plt.imshow(lum_img)

plt.show()