import cv2
import numpy as np


def floodfill_image(image):

    # change background to white
    im_floodfill_background = image.copy()
    cv2.floodFill(im_floodfill_background, None, (0, 0), 255)

    th, im_th = cv2.threshold(im_floodfill_background, 254, 255, cv2.THRESH_BINARY_INV);

    kernel = np.ones((2, 2), np.uint8)
    im_out = cv2.morphologyEx(im_th, cv2.MORPH_CLOSE, kernel, iterations=2)

    return im_out