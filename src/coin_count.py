import cv2
import os
import datetime
import numpy as np
from src.diameter_calculation import calculate_diameter
from src.floodfill import floodfill_image
from src.sum_coin import calculate_total_value


def calculate_coin_color(image, coin):
    # Calcula a cor média da moeda com base nos pixels que a compõem
    coin_pixels = np.array(coin['pixels'])
    coin_color = image[coin_pixels[:, 0], coin_pixels[:, 1]].mean(axis=0)
    return tuple(coin_color.astype(int))


def read_img(path_image):
    # Carrega a imagem
    image = cv2.imread(path_image)

    # Converte a imagem para o espaço de cores HSV e extrai o canal de valor
    image_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    image_gray = image_hsv[:, :, 2]

    # Aplica o algoritmo de preenchimento de região para binarizar a imagem
    binarized_image = floodfill_image(image_gray)

    # Calcula o diâmetro das moedas presentes na imagem
    coins = calculate_diameter(binarized_image)

    for coin in coins:
        center_y, center_x = coin['center']
        radius = coin['diameter'] // 2
        # Desenha as linhas de diâmetro para cada moeda
        cv2.line(image, (center_x - radius, center_y), (center_x + radius, center_y), (0, 255, 0), 2)
        cv2.line(image, (center_x, center_y - radius), (center_x, center_y + radius), (0, 0, 255), 2)

        # Calcula a cor da moeda com base nos pixels que a compõem
        coin_color = calculate_coin_color(image, coin)
        coin['color'] = coin_color

        # Adiciona o diâmetro na imagem
        cv2.putText(image, f"Diameter: {coin['diameter']}", (center_x - radius, center_y + radius + 20),
                    cv2.FONT_HERSHEY_DUPLEX, 0.5, (0, 0, 0), 2)

    # Salva a imagem na pasta "results" com o nome baseado na data, hora e segundo
    save_image(image, path_image)

    # Calcula o valor total das moedas presentes na imagem
    total_value = calculate_total_value(coins)
    print(f'{total_value:.2f}')


def save_image(image, path_image):
    # Obtém a data e hora atual
    current_time = datetime.datetime.now()

    # Cria o nome do arquivo com base no nome da imagem, data, hora e segundo
    filename = f"results/{os.path.splitext(os.path.basename(path_image))[0]}_{current_time.strftime('%Y%m%d_%H%M%S')}.jpg"

    # Salva a imagem no arquivo
    cv2.imwrite(filename, image)
