import cv2

filename = 'img/eyenix.jpeg'
videoname = 'img/eyenix.mp4'

original = cv2.imread(filename, cv2.IMREAD_COLOR)
cv2.imshow('Original', original)

capture = cv2.VideoCapture(videoname)

while True:
    if(capture.get(cv2.CAP_PROP_POS_FRAMES) == capture.get(cv2.CAP_PROP_FRAME_COUNT)):
        capture.open(videoname)
    ret, frame = capture.read()
    cv2.imshow("VideoFrame", frame)

    if cv2.waitKey(33) > 0: break #pressing any key is terminated

capture.release()
cv2.destroyAllWindows()
