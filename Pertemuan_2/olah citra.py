
import cv2 

#process baca citra Apel
image = cv2.imread("apple.jpg")

#proses konversi citra
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
ret, thresholding = cv2.threshold ( gray, 127, 255, cv2.THRESH_BINARY)

#tampilkan citra
cv2.imshow("Citra RGB", image)
cv2.imshow("Citra Grayscale", gray)
cv2.imshow("Citra Biner", thresholding)

cv2.waitKey(0)
cv2.destroyAllWindows()