import cv2
from src.diameter_calculation import calculate_diameter
from src.floodfill import floodfill_image
from src.sum_coin import calculate_total_value


def read_img(path_image):
    image = cv2.imread(path_image)

    # Convert the image to HSV color space
    image_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # Use only the value channel
    image_gray = image_hsv[:,:,2]

    binarized_image = floodfill_image(image_gray)

    coins = calculate_diameter(binarized_image)

    # Desenhe as linhas de diâmetro para cada moeda
    for coin in coins:
        center_y, center_x = coin['center']
        radius = coin['diameter'] // 2
        cv2.line(image, (center_x - radius, center_y), (center_x + radius, center_y), (0, 255, 0), 2)
        cv2.line(image, (center_x, center_y - radius), (center_x, center_y + radius), (0, 0, 255), 2)

        # Adiciona o diâmetro na imagem
        cv2.putText(image, f"Diameter: {coin['diameter']}", (center_x - radius, center_y + radius + 20),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

    cv2.imshow('Imagem', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    total_value = calculate_total_value(coins)
    print(f'O valor total das moedas na imagem é de R$ {total_value:.2f}')

