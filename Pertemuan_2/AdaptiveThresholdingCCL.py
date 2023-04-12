import cv2

image = cv2.imread("task4.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blur = cv2.medianBlur(gray,5)

ret, thresholding = cv2.threshold (gray,110,255,cv2.THRESH_BINARY)
adaptif_th_mean = cv2.adaptiveThreshold (blur,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,2)
adaptif_th_gaussian  = cv2.adaptiveThreshold (blur,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)



cv2.imshow("Citra RGB", image)
cv2.imshow("Citra Grayscale", gray)
cv2.imshow("citra hasil blurring", blur)
cv2.imshow("citra hasil thres binary", thresholding)
cv2.imshow("citra mean", adaptif_th_mean)
cv2.imshow("citra gaussian", adaptif_th_gaussian)
cv2.waitKey(0)
cv2.destroyAllWindow()