import numpy as np


def calculate_diameter(binarized_image):
    # Obtém a altura e largura da imagem binarizada
    height, width = binarized_image.shape

    # Cria uma matriz de booleanos do mesmo formato da imagem binarizada, inicializada com False
    visited = np.zeros_like(binarized_image, dtype=np.bool_)

    # Lista para armazenar as informações das moedas encontradas
    coins = []

    # Itera sobre cada coordenada (y, x) na imagem binarizada
    for y in range(height):
        for x in range(width):
            # Verifica se o pixel é branco (valor 255) e ainda não foi visitado
            if binarized_image[y, x] == 255 and not visited[y, x]:
                # Lista para armazenar as coordenadas dos pixels da moeda atual
                coin_pixels = [(y, x)]

                # Variável para controlar o índice atual na lista coin_pixels
                i = 0

                # Loop para expandir a área da moeda atual
                while i < len(coin_pixels):
                    # Obtém as coordenadas do pixel atual
                    cy, cx = coin_pixels[i]

                    # Verifica os pixels vizinhos (incluindo diagonalmente)
                    for dy in [-1, 0, 1]:
                        for dx in [-1, 0, 1]:
                            # Calcula as novas coordenadas
                            ny, nx = cy + dy, cx + dx

                            # Verifica se as novas coordenadas estão dentro dos limites da imagem
                            # e se o pixel é branco e ainda não foi visitado
                            if (0 <= ny < height) and (0 <= nx < width) and (binarized_image[ny, nx] == 255) and not \
                            visited[ny, nx]:
                                # Adiciona as novas coordenadas à lista coin_pixels
                                coin_pixels.append((ny, nx))

                                # Marca o pixel como visitado
                                visited[ny, nx] = True
                    i += 1

                # Encontra as coordenadas mínimas e máximas da moeda para calcular o centro e o diâmetro
                min_y = min(coin_pixels, key=lambda p: p[0])[0]
                max_y = max(coin_pixels, key=lambda p: p[0])[0]
                min_x = min(coin_pixels, key=lambda p: p[1])[1]
                max_x = max(coin_pixels, key=lambda p: p[1])[1]

                # Calcula o centro da moeda e seu diâmetro
                center_y = (min_y + max_y) // 2
                center_x = (min_x + max_x) // 2
                diameter = max(max_y - min_y, max_x - min_x)

                # Armazena as informações da moeda atual em um dicionário e adiciona à lista coins
                coins.append({'center': (center_y, center_x), 'diameter': diameter, 'pixels': coin_pixels})

    # Retorna a lista com as informações das moedas encontradas
    return coins
