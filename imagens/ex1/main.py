import os
from PIL import Image
for f in os.listdir('.//imagens'):
    logo = Image.open('catlogo.png')
    img = Image.open(f'.//imagens//{f}')
    largura, altura = img.size
    larguralogo, alturalogo = int(largura/5), int(altura/5)
    logo = logo.resize((largura, altura))
    img.paste(logo,(largura-larguralogo,altura-alturalogo),mask=logo)
    img.save(f'.//imagens//imgs{f}')
