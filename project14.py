from PIL import Image


image = Image.open("monro.jpg")
RGB_image = image.convert('RGB')
RED, GREEN, BLUE  = image.split()

coordinates_middle  = (50, 0, image.width - 50, image.height)
coordinates_left  = (100, 0, image.width, image.height)
coordinates_right  = (0, 0, image.width - 100, image.height)

RED_middle = RED.crop(coordinates_middle)
RED_left = RED.crop(coordinates_left)
RED_cropped = Image.blend(RED_middle, RED_left, 0.5)

BLUE_middle = BLUE.crop(coordinates_middle)
BLUE_right = BLUE.crop(coordinates_right)
BLUE_cropped = Image.blend(BLUE_middle, BLUE_right, 0.5)

GREEN_cropped = GREEN.crop(coordinates_middle)

image_final = Image.merge('RGB',(RED_cropped, BLUE_cropped, GREEN_cropped))

image_final.thumbnail((80, 80))
image_final.save('img_small.jpg')

