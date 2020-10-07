import cv2 

grayImg = cv2.imread('img/eyenix.jpeg', cv2.IMREAD_GRAYSCALE) 
cv2.imwrite('result_img/save.jpg', grayImg) 
cv2.imshow('gray', grayImg) 
cv2.waitKey(0) 
cv2.destroyAllWindows()

