import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
img = cv.imread('IMages\Back_to_the_Future.jpg')
 
cv.imshow('sample image',img)
hist = cv.calcHist(img,[2],None,[256],[0,256])

plt.hist(img.ravel(),256,[0,256]); plt.show()

cv.waitKey(0) # waits until a key is pressed
cv.destroyAllWindows() # destroys the window showing image