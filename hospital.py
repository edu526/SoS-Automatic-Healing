import cv2
import numpy as np # It is used to operate with any numerical data

def getPosition():
    img_rgb = cv2.imread('images/screen.png')
    template = cv2.imread('images/hospital.png')

    # Image size screen.png
    w, h = template.shape[:-1]

    # Function used to detect if an image is contained in another
    res = cv2.matchTemplate(img_rgb, template, cv2.TM_CCOEFF_NORMED)

    # Umbral admitido
    threshold = .4

    # If it is within the threshold, create a square on the image contained in the image All
    loc = np.where(res >= threshold)
    if len(loc[0]) > 1:
        x = loc[0][0]
        y = loc[1][0]
        return (x,y)

    return (0,0)