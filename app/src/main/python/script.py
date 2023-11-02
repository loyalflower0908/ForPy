import cv2

def image_gray(raw_img):
    img = cv2.imread(raw_img)
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imwrite(raw_img, img_gray)
