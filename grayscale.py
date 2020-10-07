import cv2

filename = 'img/eyenix.jpeg'

src = cv2.imread(filename, cv2.IMREAD_COLOR)

dst = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)

cv2.imshow("src", src)
cv2.imshow("grayscale", dst)
cv2.imwrite("result_img/eyenix_grayscale.jpeg",dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
