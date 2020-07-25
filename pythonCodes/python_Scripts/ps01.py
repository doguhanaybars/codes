from PIL import Image ,ImageFilter

img = Image.open('pikachu.jpg')
filtered_img = img.filter(ImageFilter.BLUR)
filtered_img = img.convert('L')

print(img)
print(img.size)
print(img.mode)
#print(dir(img))
#crooked = filtered_img.rotate(90)
resize = filtered_img.resize((300,300))
resize.save("grey.png",'png')
resize.show()