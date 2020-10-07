import cv2

filename = 'img/eyenix.jpeg'

def canny(filename):
    src = cv2.imread(filename, cv2.IMREAD_COLOR)
    canny = cv2.Canny(src, 100, 255)
    cv2.imshow('canny', canny)
    cv2.imwrite('result_img/eyenix_edge_canny.jpeg', canny)

def sobel(filename):
    src = cv2.imread(filename, cv2.IMREAD_COLOR)
    gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
    sobel = cv2.Sobel(gray, cv2.CV_8U, 1, 0, 3)
    cv2.imshow('sobel', sobel)
    cv2.imwrite('result_img/eyenix_edge_sobel.jpeg', sobel)

def laplacian(filename):
    src = cv2.imread(filename, cv2.IMREAD_COLOR)
    gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
    laplacian = cv2.Laplacian(gray, cv2.CV_8U, ksize=3)
    cv2.imshow('laplacian', laplacian)
    cv2.imwrite('result_img/eyenix_edge_laplacian.jpeg', laplacian)

if __name__ == "__main__":
    img = cv2.imread(filename)
    cv2.imshow('Original', img)
    canny(filename)
    sobel(filename)
    laplacian(filename)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
