import numpy as np


def calculate_diameter(binarized_image):
    height, width = binarized_image.shape
    visited = np.zeros_like(binarized_image, dtype=np.bool_)  # Matriz para rastrear quais pixels foram visitados
    coins = []  # Lista para armazenar as moedas

    for y in range(height):
        for x in range(width):
            # Se encontra um pixel branco que não foi visitado antes, temos uma nova moeda
            if binarized_image[y, x] == 255 and not visited[y, x]:
                # Encontra todos os pixels contíguos para esta moeda
                coin_pixels = [(y, x)]
                i = 0
                while i < len(coin_pixels):
                    cy, cx = coin_pixels[i]
                    for dy in [-1, 0, 1]:
                        for dx in [-1, 0, 1]:
                            ny, nx = cy + dy, cx + dx
                            if (0 <= ny < height) and (0 <= nx < width) and (binarized_image[ny, nx] == 255) and not visited[ny, nx]:
                                coin_pixels.append((ny, nx))
                                visited[ny, nx] = True
                    i += 1

                # Encontra as coordenadas y mínimas e máximas para os pixels da moeda
                min_y = min(coin_pixels, key=lambda p: p[0])[0]
                max_y = max(coin_pixels, key=lambda p: p[0])[0]
                # Encontra as coordenadas x mínimas e máximas para os pixels da moeda
                min_x = min(coin_pixels, key=lambda p: p[1])[1]
                max_x = max(coin_pixels, key=lambda p: p[1])[1]

                # O centro da moeda é a média das coordenadas mínimas e máximas
                center_y = (min_y + max_y) // 2
                center_x = (min_x + max_x) // 2

                # O diâmetro da moeda é a maior diferença entre as coordenadas mínimas e máximas
                diameter = max(max_y - min_y, max_x - min_x)

                # Adiciona as informações da moeda à lista
                coins.append({'center': (center_y, center_x), 'diameter': diameter})

    return coins



