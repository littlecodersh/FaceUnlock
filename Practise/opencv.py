#coding=utf8
import numpy as np
import cv2

def show_picture():
    img = cv2.imread('qr.jpg', 0)
    cv2.namedWindow('image', cv2.WINDOW_NORMAL)
    cv2.imshow('image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def cap_video():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened(): print('Cap failed because of camera')

    while 1:
        # Capture frame-by-frame
        ret, frame = cap.read()
        # Our operations on the frame come here
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow('frame',gray)
        # cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()

def click_demo():
    def draw_circle(event,x,y,flags,param):
        if event==cv2.EVENT_LBUTTONDBLCLK:
            cv2.circle(img,(x,y),100,(255,255,255),-1)

    # 创建图像与窗口并将窗口与回调函数绑定
    img=np.zeros((512,512,3),np.uint8)
    cv2.namedWindow('image')
    cv2.setMouseCallback('image',draw_circle)
    while(1):
        cv2.imshow('image',img)
        if cv2.waitKey(20)&0xFF==27: break
    cv2.destroyAllWindows()

def cannyedge():
    capInput = cv2.VideoCapture(0)
    if not capInput.isOpened(): print('Cap failed because of camera')

    while 1:
        ret, img = capInput.read()
        edges = cv2.Canny(img, 80, 150)
        cv2.imshow('Edge', edges)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    # When everything done, release the capture
    capInput.release()
    cv2.destroyAllWindows()

cannyedge()
