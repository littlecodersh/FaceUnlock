import cv2, time

def get_rgb_in_video():
    imgWindow = cv2.namedWindow('ColorInVideo', cv2.WINDOW_NORMAL)
    img = None
    def show_color(event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:
            print('%s,%s: %s'%(x, y, img[y, x]))
    cv2.setMouseCallback('ColorInVideo', show_color)
    capInput = cv2.VideoCapture(0)
    if not capInput.isOpened(): print('Capture failed because of camera')
    while 1:
        ret, img = capInput.read()
        cv2.imshow('ColorInVideo', img)

        keyPress = cv2.waitKey(1) & 0xFF
        if keyPress == ord(' '):
            while cv2.waitKey(1) & 0xFF != ord(' '): time.sleep(.1)
        elif keyPress == ord('q'):
            break
    capInput.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    get_rgb_in_video()
