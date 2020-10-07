import numpy as np
import cv2

filename = 'img/eyenix.jpeg'

def blur_convolution(filename):
    img = cv2.imread(filename)
    kernel = np.ones((5,5),np.float32)/25
    blur_conv = cv2.filter2D(img, -1, kernel) 
    cv2.imshow('blur_convolution', blur_conv)
    cv2.imwrite('result_img/eyenix_blur_conv.jpeg', blur_conv)

def blur_averaging(filename):
    img = cv2.imread(filename)
    blur_average = cv2.blur(img,(5,5))
    cv2.imshow('blur_average', blur_average)
    cv2.imwrite('result_img/eyenix_blur_average.jpeg', blur_average)

def blur_Gaussian_Blurring(filename):
    img = cv2.imread(filename)
    blur_Gaussian = cv2.GaussianBlur(img,(5,5),0)
    cv2.imshow('blur_Gaussian', blur_Gaussian)
    cv2.imwrite('result_img/eyenix_blur_Gaussian.jpeg', blur_Gaussian)

def blur_Median(filename):
    img = cv2.imread(filename)
    blur_median = cv2.medianBlur(img, 5)
    cv2.imshow('blur_median', blur_median)
    cv2.imwrite('result_img/eyenix_blur_median.jpeg', blur_median)

def blur_Bilateral(filename):
    img = cv2.imread(filename)
    blur_Bilateral = cv2.bilateralFilter(img,9,75,75)
    cv2.imshow('blur_Bilateral', blur_Bilateral)
    cv2.imwrite('result_img/eyenix_blur_Bilateral.jpeg', blur_Bilateral)

if __name__ == "__main__":
    img = cv2.imread(filename)
    cv2.imshow('Original', img)
    blur_convolution(filename)
    blur_averaging(filename)
    blur_Gaussian_Blurring(filename)
    blur_Median(filename)
    blur_Bilateral(filename)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
