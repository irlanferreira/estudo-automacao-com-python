from PIL import Image, ImageColor

gato = Image.open('zophie.png')
gatocortado = gato.crop((335, 345, 565, 560))
gatocortado.save('gatocortado.png')
gatocopia = gato.copy()
gatocopia.paste(Image.open('mex.jpg').resize((100, 100)), (400, 150))
gatocopia.save('gatoemex.png')

gatogirado = gato.transpose(Image.FLIP_TOP_BOTTOM)
gatogirado.save('gatogirado.png')

cor = gato.getpixel((200, 350))
gatocolorido = gato.copy()
for x in range(200):
    for y in range(200):
        gatocolorido.putpixel((x, y), ImageColor.getrgb('Blue'))
gatocolorido.save('gatocor.png')
