import cv2
import numpy as np

def sharpness():
    img = cv2.imread("C:/Users/smokhash/Documents/image2 (1).jpg", cv2.IMREAD_COLOR)
    if img is None:
        print("Could not open or find the image")
        return
    
    kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
    blurred_img = cv2.GaussianBlur(img, (3, 3), 0)
    
    roi = cv2.selectROI("Select ROI", img, fromCenter=False, showCrosshair=True)
    if roi == (0, 0, 0, 0):
        print("No ROI selected")
        return
    
    x, y, w, h = roi
    imageroi = img[y:y+h, x:x+w]
    sharpenedRoi = cv2.filter2D(imageroi, -1, kernel)
    
    sharpenedImage = img.copy()
    sharpenedImage[y:y+h, x:x+w] = sharpenedRoi
    
    cv2.imshow("Sharpened Image", sharpenedImage)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

sharpness()