import cv2
import numpy as np
from math import sqrt

K = 3

def Convolution(input, kernel, kernel2, output, height, width):
    for i in range(height):
        for j in range(width):
            sumX = 0
            sumY = 0
            for i1 in range(-1, 2):
                for j1 in range(-1, 2):
                    ii = i + i1
                    jj = j + j1
                    if ii >= 0 and ii < height and jj >= 0 and jj < width:
                        sumX += int(input[ii * width + jj]) * kernel[(i1 + 1) * 3+ (j1 + 1)]
                        sumY += int(input[ii * width + jj]) * kernel2[(i1 + 1) * 3 + (j1 + 1)]
            
            sum = sqrt(sumX * sumX + sumY * sumY)
            if sum > 255:
                sum = 255
            output[i * width + j] = int(sum)

def SobelImage():
    img = cv2.imread("C:/Users/smokhash/Documents/image2 (1).jpg", cv2.IMREAD_COLOR)
    if img is None:
        print("Could not open or find the image")
        exit()

    rows, cols, channels = img.shape

    
    bluechannel, greenchannel, redchannel = cv2.split(img)

    
    blue = bluechannel.flatten()
    green = greenchannel.flatten()
    red = redchannel.flatten()

    Kernel = [-1, 0, 1, -2, 0, 2, -1, 0, 1]
    Kernel2 = [-1, -2, -1, 0, 0, 0, 1, 2, 1]

 
    grad_B = np.zeros_like(blue)
    grad_G = np.zeros_like(green)
    grad_R = np.zeros_like(red)

   
    Convolution(blue, Kernel, Kernel2, grad_B, rows, cols)
    Convolution(green, Kernel, Kernel2, grad_G, rows, cols)
    Convolution(red, Kernel, Kernel2, grad_R, rows, cols)

  
    grad_B = grad_B.reshape((rows, cols))
    grad_G = grad_G.reshape((rows, cols))
    grad_R = grad_R.reshape((rows, cols))

   
    final_output = cv2.merge([grad_B, grad_G, grad_R])

    
    cv2.imshow("Original Image", img)
    cv2.imshow("Sobel", final_output)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def SobelVideo():
    cap = cv2.VideoCapture('C:/Users/smokhash/Documents/firstvideo.mp4')
    
    if not cap.isOpened():
        print("Error opening video stream or file")
        return

    Kernel = np.array([-1, 0, 1, -2, 0, 2, -1, 0, 1]).reshape((3, 3))
    Kernel2 = np.array([-1, -2, -1, 0, 0, 0, 1, 2, 1]).reshape((3, 3))

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        fps = int(cap.get(cv2.CAP_PROP_FPS))
        rows, cols = frame.shape[:2]
        bluechannel, greenchannel, redchannel = cv2.split(frame)
        
        grad_B = cv2.filter2D(bluechannel, -1, Kernel) + cv2.filter2D(bluechannel, -1, Kernel2)
        grad_G = cv2.filter2D(greenchannel, -1, Kernel) + cv2.filter2D(greenchannel, -1, Kernel2)
        grad_R = cv2.filter2D(redchannel, -1, Kernel) + cv2.filter2D(redchannel, -1, Kernel2)
        
        final_output = cv2.merge([grad_B, grad_G, grad_R])
         
        filename = "frame_"+str(fps)+".jpg"
        cv2.imwrite(filename,frame)
        fps = fps+1
        cv2.imshow('Frame', frame)
        cv2.imshow('Sobel', final_output)
        
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


SobelImage()
SobelVideo()