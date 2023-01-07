import cv2 as cv
from resize import rescalFrame


# read image
# img = cv.imread('Photos/cat_large.jpg') 
# cv.imshow("Cat", img)

# print(img)
# cv.waitKey(0)





# reading video
capture = cv.VideoCapture('Videos/dog.mp4')


while True:
    isTrue, frame = capture.read()
    frame_resized = rescalFrame(frame=frame,scale=0.2)
    if isTrue:
        cv.imshow("Video", frame)
        cv.imshow("Reszied video", frame_resized)
        if cv.waitKey(20) & 0xFF==ord('d'):
            break
    else:
        break

capture.release()   
cv.destroyAllWindows()

cv.waitKey(0)
