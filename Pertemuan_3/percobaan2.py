from PIL import Image
import numpy as np
im = np.array(Image.open('kucing.jpg'))
im_R = im.copy()
im_R[:, :, (1, 2)] = 0
im_G = im.copy()
im_G[:, :, (0, 2)] = 0
im_B = im.copy()
im_B[:, :, (0, 1)] = 0
im_RGB = np.concatenate((im_R, im_G, im_B),
axis=1)
pil_img = Image.fromarray(im_RGB)
pil_img.save('kucing1.jpg')