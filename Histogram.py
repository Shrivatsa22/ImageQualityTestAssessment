import cv2
import numpy as np

def histogram(input, output, height, width):
   for i in range(height):
       for j in range(width):
           count = input[i * width + j]
           output[count] += 1

def plothistogram(histogramB, histogramG, histogramR):
   hist_w = 300
   hist_h = 412
   bin_w = round(hist_w / 256)
  
   histImage = np.zeros((hist_h, hist_w, 3), dtype=np.uint8)

   max_value = max(max(histogramB), max(histogramG), max(histogramR))
   
   for i in range(256):
       histogramB[i] = int((histogramB[i] / max_value) * hist_h)
       histogramG[i] = int((histogramG[i] / max_value) * hist_h)
       histogramR[i] = int((histogramR[i] / max_value) * hist_h)
   
   for i in range(1, 256):
      
       cv2.line(histImage, (bin_w * (i - 1), hist_h - histogramB[i - 1]),
                (bin_w * i, hist_h - histogramB[i]), (255, 0, 0), 2)
       
       cv2.line(histImage, (bin_w * (i - 1), hist_h - histogramG[i - 1]),
                (bin_w * i, hist_h - histogramG[i]), (0, 255, 0), 2)
     
       cv2.line(histImage, (bin_w * (i - 1), hist_h - histogramR[i - 1]),
                (bin_w * i, hist_h - histogramR[i]), (0, 0, 255), 2)
  
   #cv2.imshow("Histogram", histImage)
   cv2.waitKey(0) 
   cv2.destroyAllWindows()

def DisplayImage():
   img = cv2.imread("C:/Users/smokhash/Documents/image2 (1).jpg", cv2.IMREAD_COLOR)
   if img is None:
       print("Could not open or find the image")
       exit()
   
   rows, cols, channels = img.shape
   bluechannel, greenchannel, redchannel = cv2.split(img)
   #cv2.imshow("image",img)
 
   blue = bluechannel.flatten()
   green = greenchannel.flatten()
   red = redchannel.flatten()
  
   grad_B = np.zeros(256, dtype=int)
   grad_G = np.zeros(256, dtype=int)
   grad_R = np.zeros(256, dtype=int)
 
   histogram(blue, grad_B, rows, cols)
   histogram(green, grad_G, rows, cols)
   histogram(red, grad_R, rows, cols)
   
   plothistogram(grad_B, grad_G, grad_R)
   

#DisplayImage()