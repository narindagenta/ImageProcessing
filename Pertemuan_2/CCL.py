import cv2
import numpy as np

image = cv2.imread('task4.jpg')

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray_correct = np.array(100 * (gray/255) ** 1.2 , dtype='uint8')
gray_equ = cv2.equalizeHist(gray)
thresh = cv2.adaptiveThreshold(gray_correct, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 255 , 10)

kernel = np.ones((15,15), np.uint8)
img_dilation = cv2.dilate(thresh, kernel, iterations=1)
img_erode = cv2.erode(img_dilation, kernel, iterations=1)

img_erode = cv2.medianBlur(img_erode, 7)

ret, labels = cv2.connectedComponents(img_erode)
label_hue = np.uint8(179 * labels/np.max(labels))
blank_ch = 255 * np.ones_like(label_hue)
labeled_img = cv2.merge ([label_hue, blank_ch, blank_ch])
labeled_img =cv2.cvtColor (labeled_img, cv2.COLOR_HSV2BGR)
labeled_img[label_hue ==0] = 0


cv2.imshow("citra rgb", image)
cv2.imshow("citra grayscale", thresh)
cv2.imshow("dilation + erosin", img_erode)
cv2.imshow("jumlah objek =" + str(ret-1), labeled_img)

cv2.waitKey(0)
cv2.destroyAllWindows()