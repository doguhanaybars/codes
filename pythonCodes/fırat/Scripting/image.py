from PIL import Image, ImageFilter

img = Image.open('./Scripting/pokedex/pikachu.jpg')

filtered_image = img.convert("L")
filtered_image.save("grey.png", "png")
# filtered_image.show()
crooked = filtered_image.rotate(90)
# filtered_image.show()
crooked.save("crooked.png", "png")
