#Mengimpor data gambar ke dalam array Numpy

import matplotlib.pyplot as plt 
import matplotlib.image as mping

from PIL import Image

img=mping.imread('kucing.jpg')

lum_img = img[:,:, 0] 

plt.imshow(lum_img, cmap="hot")

plt.show()