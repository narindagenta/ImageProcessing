import cv2
#Proses Baca Citra Apel
image = cv2.imread("task4.jpg")
#Proses Konversi Citra
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
#Proses Blur citra apel
blur= cv2.GaussianBlur(gray, (9,9),0)
#Proses Thresholding
ret, thresholding = cv2.threshold(gray, 120, 255, cv2.THRESH_BINARY)
#otsu binarizationations
ret2, otsu_binarization = cv2.threshold (gray, 10, 255, cv2 .THRESH_BINARY + cv2.THRESH_OTSU)
#otsu binarizations afther gaussian blur
ret3, otsu_binarization2 = cv2.threshold (blur, 10, 255 , cv2 .THRESH_BINARY + cv2.THRESH_OTSU)
#Tampilkan Citra
cv2.imshow("Catra RGB", image)
cv2.imshow("Citra Grayscale",gray)
cv2.imshow("Citra Hasil Blurring", blur)
cv2.imshow("Citra Hasil Thres Binary", thresholding)
cv2.imshow("otsu binarizations", otsu_binarization)
cv2.imshow("otsu binarizations afther gaussian blur", otsu_binarization2)
cv2.waitKey(0)
cv2.destroyAl1Windows()