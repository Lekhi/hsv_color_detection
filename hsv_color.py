import cv2
import numpy as np


def nothing(x):
    pass


lower_limit = np.array([0, 0, 0])
upper_limit = np.array([180, 255, 255])


def mouse_callback(event, x, y, flags, param):
    global lower_limit, upper_limit
    if event == cv2.EVENT_LBUTTONDOWN:
        h = hsv[y, x, 0]
        s = hsv[y, x, 1]
        v = hsv[y, x, 2]
        print('Hue = ', h)
        print('Saturation = ', s)
        print('Value = ', v)
        #if lower_limit is None:
        lower_limit = np.array([h-10, s-40, v-40])
        #elif upper_limit is None:
        upper_limit = np.array([h+10, s+40, v+40])



capture = cv2.VideoCapture('rgb_ball_720.mp4')


cv2.namedWindow('Trackbars')

cv2.namedWindow('frame')
cv2.setMouseCallback('frame', mouse_callback)

cv2.createTrackbar('L - H', 'Trackbars', 0, 179, nothing)
cv2.createTrackbar('L - S', 'Trackbars', 0, 255, nothing)
cv2.createTrackbar('L - V', 'Trackbars', 0, 255, nothing)
cv2.createTrackbar('U - H', 'Trackbars', 0, 179, nothing)
cv2.createTrackbar('U - S', 'Trackbars', 0, 255, nothing)
cv2.createTrackbar('U - V', 'Trackbars', 0, 255, nothing) 

while True:
    _, frame = capture.read() 
    # changing frame color format from RGB to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    l_h = cv2.getTrackbarPos('L - H', 'Trackbars')
    l_s = cv2.getTrackbarPos('L - S', 'Trackbars')
    l_v = cv2.getTrackbarPos('L - V', 'Trackbars')
    u_h = cv2.getTrackbarPos('U - H', 'Trackbars')
    u_s = cv2.getTrackbarPos('U - S', 'Trackbars')
    u_v = cv2.getTrackbarPos('U - V', 'Trackbars')

    lower_red = np.array([l_h, l_s, l_v])
    upper_red = np.array([u_h, u_s, u_v])
    mask = cv2.inRange(hsv, lower_limit, upper_limit)

    contour = cv2.findContours(mask.copy(),
                                cv2.RETR_EXTERNAL,
                                cv2.CHAIN_APPROX_SIMPLE)[-2]
    if len(contour) > 0:
        ball_area = max(contour, key=cv2.contourArea)
        (xg, yg, wg, hg) = cv2.boundingRect(ball_area)
        cv2.rectangle(frame, (xg, yg), (xg + int(1.1*wg), yg + int(hg*1.1)), (0, 255, 0), 2)


    cv2.imshow('frame', frame)
    cv2.imshow('mask', mask)
    
    key = cv2.waitKey(1)
    if key == 27:
        break
    if key == ord('p'):
        cv2.waitKey(-1)


capture.release()
cv2.destroyAllWindows()
