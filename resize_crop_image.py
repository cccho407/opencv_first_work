import cv2

filename = 'img/eyenix.jpeg'

src = cv2.imread(filename, cv2.IMREAD_COLOR)

resize_img = cv2.resize(src, dsize=(700, 300), interpolation=cv2.INTER_AREA)
cropped_img = src[100:200,200:500]

cv2.imshow("src", src)
cv2.imshow("resize_img", resize_img)
cv2.imshow("cropped_img", cropped_img)

cv2.imwrite('result_img/eyenix_resize.jpeg', resize_img)
cv2.imwrite('result_img/eyenix_cropped.jpeg', cropped_img)

cv2.waitKey(0) #pressing any key is treminated
cv2.destroyAllWindows()
