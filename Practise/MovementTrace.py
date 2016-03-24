import cv2, numpy

capInput = cv2.VideoCapture(0)
baseImg = None

while 1:
    ret, img = capInput.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (21,21), 0)
    if not gray is None: baseImg = gray;break

while 1:
    ret, img = capInput.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (21,21), 0)

    imgDelta = cv2.absdiff(baseImg, gray)
    mask = cv2.threshold(imgDelta, 25, 255, cv2.THRESH_BINARY)[1]
    kernel = numpy.ones((5,5), numpy.uint8)
    mask = cv2.erode(mask,kernel,iterations = 1)

    result = cv2.bitwise_and(img, img, mask = mask)

    cv2.imshow('img', img)
    cv2.imshow('mask', mask)
    cv2.imshow('result', result)

    if cv2.waitKey(1) & 0xFF == 27: break

capInput.release()
cv2.destroyAllWindows()
