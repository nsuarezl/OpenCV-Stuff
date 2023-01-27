import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
from matplotlib.widgets import Slider

img = cv.imread('IMages\dog.bmp')
img2 = cv.imread('IMages\south_L-150x150.png')
hist= plt.hist(img.ravel(),256,[0,256])
hist2= plt.hist(img2.ravel(),256,[0,256])

# Read the image
img = cv.imread("IMages\dog.bmp")

# Create figure and axis
fig, ax = plt.subplots()
plt.subplots_adjust(bottom=0.5)
fig.set_size_inches(10,10)
ax1 = fig.add_subplot(2, 2, 1)
ax2 = fig.add_subplot(2, 2, 2)
ax3 = fig.add_subplot(2, 2, 3)
ax4 = fig.add_subplot(2, 2, 4)

# Display the image

im = ax1.imshow(cv.cvtColor(img, cv.COLOR_BGR2RGB))
im2 = ax2.imshow(cv.cvtColor(img2, cv.COLOR_BGR2RGB))
ax3.hist(img.ravel(), bins=256, color = 'r')
ax4.hist(img2.ravel(), bins=256, color = 'g')
# Create contrast and brightness sliders
ax_c = plt.axes([0.25, 0.1, 0.65, 0.03], facecolor='lightgoldenrodyellow')
ax_b = plt.axes([0.25, 0.15, 0.65, 0.03], facecolor='lightgoldenrodyellow')

s_c = Slider(ax_c, 'Contrast', 0.5, 2.0, valinit=1)
s_b = Slider(ax_b, 'Brightness', -0.5, 0.5, valinit=0)

ax_d = plt.axes([0.25, 0.2, 0.65, 0.03], facecolor='lightgoldenrodyellow')
ax_e = plt.axes([0.25, 0.25, 0.65, 0.03], facecolor='lightgoldenrodyellow')

s_d = Slider(ax_d, 'Contrast', 0.5, 2.0, valinit=1)
s_e = Slider(ax_e, 'Brightness', -0.5, 0.5, valinit=0)

# Define update function
def update(val):
    contrast = s_c.val
    brightness = s_b.val
    img_c = img.copy()
    img_c = cv.convertScaleAbs(img_c, alpha=contrast, beta=brightness*255)
    im.set_data(cv.cvtColor(img_c, cv.COLOR_BGR2RGB))
    fig.canvas.draw_idle()

# Connect update function to sliders
s_c.on_changed(update)
s_b.on_changed(update)

def update1(val):
    contrast = s_d.val
    brightness = s_e.val
    img_c = img2.copy()
    img_c = cv.convertScaleAbs(img_c, alpha=contrast, beta=brightness*255)
    im2.set_data(cv.cvtColor(img_c, cv.COLOR_BGR2RGB))
    fig.canvas.draw_idle()

# Connect update function to sliders
s_d.on_changed(update1)
s_e.on_changed(update1)

# Show the figure
plt.show()