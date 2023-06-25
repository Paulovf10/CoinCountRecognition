from collections import defaultdict


def classify_coins_by_diameter(coins):
    # Agrupa as moedas por diâmetro, aceitando uma diferença de até 3 no valor do diâmetro
    grouped_coins = defaultdict(list)

    for coin in coins:
        # Encontra grupo existente mais próximo do diâmetro da moeda
        for group_diameter in grouped_coins:
            if abs(group_diameter - coin['diameter']) <= 3:
                grouped_coins[group_diameter].append(coin)
                break
        else:
            # Se não encontramos nenhum grupo existente, criamos um novo
            grouped_coins[coin['diameter']].append(coin)

    return grouped_coins


def calculate_total_value(coins):
    grouped_coins = classify_coins_by_diameter(coins)
    total_value = 0

    # Ordena os grupos de moedas pelo diâmetro
    sorted_groups = sorted(grouped_coins.items())
    # Atribui valores às moedas em cada grupo, do menor ao maior
    coin_values = [0.10, 0.05, 0.50, 0.25,  1.00]

    for i, (diameter, coins) in enumerate(sorted_groups):
        coin_value = coin_values[min(i, len(coin_values) - 1)]
        total_value += coin_value * len(coins)

    return total_value

