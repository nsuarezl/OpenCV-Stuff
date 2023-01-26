import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread('IMages\dog.BMP')
img2 = cv.imread('IMages\south_L-150x150.png')
imgR = cv.resize(img,(150,150))
Hori = np.concatenate((imgR, img2), axis=1)
fig = plt.figure(figsize=(10, 7))

cv.imshow('HORIZONTAL', Hori)

hist = cv.calcHist(img,[2],None,[256],[0,256])
imgAndHist = np.concatenate((Hori,hist), axis=0)
plt.hist(img.ravel(),256,[0,256]); plt.show()

cv.waitKey(0) # waits until a key is pressed
cv.destroyAllWindows() # destroys the window showing image