import cv2
import numpy as np


def floodfill_image(image):

    # change background to white
    im_floodfill_background = image.copy()
    cv2.floodFill(im_floodfill_background, None, (0, 0), 255)

    th, im_th = cv2.threshold(im_floodfill_background, 254, 255, cv2.THRESH_BINARY_INV);

    # Invert floodfilled image
    im_floodfill_inv = cv2.bitwise_not(im_floodfill_background)

    # Combine the two images to get the foreground
    im_out = im_th | im_floodfill_inv

    return im_out