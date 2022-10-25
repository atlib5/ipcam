import urllib.request
import cv2
import numpy as np
import imutils
import random
r1 = random.randint(0, 1000)
print( str(r1))
print(type(r1))
url='http://192.168.1.21:8080/shot.jpg'
imgPath = urllib.request.urlopen(url)
imgNp = np.array(bytearray(imgPath.read()), dtype=np.uint8)
img = cv2.imdecode(imgNp, -1)
            
img = imutils.resize(img, width=700)
cv2.imwrite(str(r1)+'im.jpg',img)
cv2.imshow("pantech", img)
cv2.waitKey(5000)


        
