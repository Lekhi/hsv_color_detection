import cv2
#Read pictures and zoom for easy display
img=cv2.imread("random_image.jpg")
height, width=img.shape[:2]
size=(int(width * 0.2), int(height * 0.2))
#Zoom
img=cv2.resize(img, size, interpolation=cv2.inter_area)
#bgr to hsv
hsv=cv2.cvtcolor(img, cv2.color_bgr2hsv)
#Mouse click response event
def getposhsv(event, x, y, flags, param):
    if event==cv2.event_lbuttondown:
        print("hsv is", hsv[y, x])
def getposbgr(event, x, y, flags, param):
    if event==cv2.event_lbuttondown:
        print("bgr is", img[y, x])
cv2.imshow("imagehsv", hsv)
cv2.imshow("image", img)
cv2.setmousecallback("imagehsv", getposhsv)
cv2.setmousecallback("image", getposbgr)
cv2.waitkey(0)
