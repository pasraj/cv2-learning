import cv2 as cv
def rescalFrame(frame, scale=0.75):
    # Image, Video, Live Videos
    try:
        width = int(frame.shape[1] * scale)
        height = int(frame.shape[0] * scale)
        dimensions = (width, height)
        return cv.resize(frame,dimensions, interpolation=cv.INTER_AREA)
    except:
        pass
