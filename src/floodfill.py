import cv2
import numpy as np


def floodfill_image(image):
    # Use the Canny edge detector to find edges in the image
    edges = cv2.Canny(image, 50, 150)

    # Use a morphological closing operation to close gaps in the edges
    kernel = np.ones((3, 3), np.uint8)
    closing = cv2.morphologyEx(edges, cv2.MORPH_CLOSE, kernel)

    # Flood fill from point (0, 0), using the closed edges as the mask
    im_floodfill = closing.copy()
    h, w = closing.shape[:2]
    mask = np.zeros((h+2, w+2), np.uint8)
    cv2.floodFill(im_floodfill, mask, (20, 0), 255)

    # Invert floodfilled image
    im_floodfill_inv = cv2.bitwise_not(im_floodfill)

    # Combine the two images to get the foreground
    im_out = closing | im_floodfill_inv

    return im_out
