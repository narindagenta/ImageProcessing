#mengubah ukuran gambar contoh op pikse;
import matplotlib.pyplot as plt
from PIL import Image

img= Image.open('kucing.jpg')
img.thumbnail((64,64), Image.ANTIALIAS)
plt.imshow (img)

plt.show()