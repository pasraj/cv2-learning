import cv2 as cv


img = cv.imread('Photos/cat.jpg')
cv.imshow("Cat", img)


# change into gray image
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray", gray)


# Blur
blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
cv.imshow("Blur", blur)

# Edge cascade
canny = cv.Canny(img, 125,175)
cv.imshow("Canny Edge",canny)


# Dialating the image 

dilated = cv.dilate(canny,(3,3), iterations=2)
cv.imshow("Dilated", dilated)


resized = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
cv.imshow("Resized", resized)


croped = img[50:200, 200:400]
cv.imshow("Croped", croped)

cv.waitKey(0)