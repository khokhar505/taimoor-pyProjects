from PIL import Image

pic = Image.open('small.png')
bg = Image.open('large.jpg')
bg.paste(pic)

bg.show()