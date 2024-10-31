from PIL import Image


image = Image.open("monro.jpg")
rgb_image = image.convert('RGB')
red, green, blue = image.split()

coordinates_middle  = (50, 0, image.width - 50, image.height)
coordinates_left  = (100, 0, image.width, image.height)
coordinates_right  = (0, 0, image.width - 100, image.height)

red_middle = red.crop(coordinates_middle)
red_left = red.crop(coordinates_left)
red_cropped = Image.blend(red_middle, red_left, 0.5)

blue_middle = blue.crop(coordinates_middle)
blue_right = blue.crop(coordinates_right)
blue_cropped = Image.blend(blue_middle, blue_right, 0.5)

green_cropped = green.crop(coordinates_middle)

image_final = Image.merge('RGB',(red_cropped, green_cropped, blue_cropped))

image_final.thumbnail((80, 80))
image_final.save('img_small.jpg')

