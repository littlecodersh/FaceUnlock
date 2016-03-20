import cv2, numpy

capInput = cv2.VideoCapture(0)

while 1:
    ret, img = capInput.read()
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    lower_color = numpy.array([100, 80, 80])
    upper_color = numpy.array([150, 255, 255])

    mask = cv2.inRange(hsv, lower_color, upper_color)
    result = cv2.bitwise_and(img, img, mask = mask)

    cv2.imshow('img', img)
    cv2.imshow('mask', mask)
    cv2.imshow('result', result)

    if cv2.waitKey(1) & 0xFF == 27: break

capInput.release()
cv2.destroyAllWindows()
