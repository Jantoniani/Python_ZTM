from PIL import Image, ImageFilter

img = Image.open('pikachu.jpg')
filtered_img = img.filter(ImageFilter.BLUR)
smooth_img = img.filter(ImageFilter.SMOOTH)
converted_img = img.convert('L')
crooked_img = img.rotate(90)
resize_img = img.resize((300, 300))


img2 = Image.open('Warrior.jpg')
img2.thumbnail((400, 400))
img2.save('Warrior_Thumbnail.jpg')



box = (100, 100, 400, 400)
cropped_img = img.crop(box)



print(img.format)
print(img.size)
print(img.mode)
print(img)
print(img2.size)

filtered_img.save('blur.png', 'png')
smooth_img.save('smooth.png', 'png')
converted_img.save('grayscale.png', 'png')
crooked_img.save('crooked.png', 'png')
resize_img.save('resize.png', 'png')
cropped_img.save('cropped.png', 'png')

filtered_img.show()