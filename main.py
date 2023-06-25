import os
from src.coin_count import read_img


print("------------------------------------------------------------------")
print("                   $$$ Contador de moedas $$$")
print("------------------------------------------------------------------")
while True:
    #input_user = input("Por favor, insira o caminho para a imagem: ")
    #path_image = f"static/{input_user}"
    path_image = f"static/teste5.png"
    if os.path.isfile(path_image):
        read_img(path_image)
    else:
        print("Arquivo não encontrado. Por favor, tente novamente.")
    break



