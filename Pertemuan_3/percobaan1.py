import cv2 
import matplotlib.pyplot as plt

img = cv2.imread('lamborgini.jpg')

img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
gray_img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY) 

gray = cv2.cvtColor(gray_img, cv2.COLOR_GRAY2RGB)

print (gray_img)

plt.imshow(gray)

plt.show()