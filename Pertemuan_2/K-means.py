import cv2
import numpy as np

image = cv2.imread('task3.jpg')
z = image.reshape ((-1,3))

z = np.float32(z)

criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
K = 32
ret, label, center = cv2.kmeans(z,K,None,criteria,10,cv2.KMEANS_RANDOM_CENTERS)
center = np.uint8(center)
res = center[label.flatten()]
res2 = res.reshape((image.shape))
cv2.imshow('hasil res',res2)
cv2.waitKey(0)
cv2.destroyAllWindows()