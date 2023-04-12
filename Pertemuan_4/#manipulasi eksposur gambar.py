#Memanipulasi eksposur gambar

import numpy as np
import matplotlib.pyplot as plt
import skimage.exposure as skie

img = plt.imread("/content/kucing.jpg")

def show(img) :
  #Display the image.
  fig, (ax1, ax2) = plt.subplots(1,2,figsize=(12,3))
  ax1.imshow(img, cmap=plt.cm.gray)
  ax1.set_axis_off()

  #Display the histogram.
  ax2.hist(img.ravel(),lw=0, bins=256)
  ax2.set_xlim(0, img.max())
  ax2.set_yticks([])
  plt.show()
show(img)

show(skie.rescale_intensity(img, in_range=(0.4, .95), out_range=(0,1)))