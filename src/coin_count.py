import cv2
from src.diameter_calculation import calculate_diameter
from src.floodfill import floodfill_image


def read_img(path_image):
    image = cv2.imread(path_image)
    image_gray = cv2.imread(path_image, cv2.IMREAD_GRAYSCALE)
    binarized_image = floodfill_image(image_gray)
    coins = calculate_diameter(binarized_image)

    # Desenhe as linhas de diâmetro para cada moeda
    for coin in coins:
        center_y, center_x = coin['center']
        radius = coin['diameter'] // 2
        cv2.line(image, (center_x - radius, center_y), (center_x + radius, center_y), (0, 255, 0), 2)
        cv2.line(image, (center_x, center_y - radius), (center_x, center_y + radius), (0, 0, 255), 2)

    cv2.imshow('Imagem', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()