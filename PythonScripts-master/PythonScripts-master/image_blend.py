
# This script accepts two command line arguments which are the filenames of the images to blended together. 
# If the images are not of the same size, the larger image will be cropped to fit into the smaller image
# sample way to usage : 
# python image_blend.py 1.png, 2.png

from PIL import Image
from resizeimage import resizeimage
import sys

arguments = sys.argv
arguments.pop(0)
first_image, second_image = arguments
background = Image.open(first_image)
overlay = Image.open(second_image)

background = background.convert("RGBA")
overlay = overlay.convert("RGBA")

if background.size != overlay.size :
	new_size = min(background.size, overlay.size)

	if new_size == overlay.size :
		background = resizeimage.resize_crop(background, list(new_size))
	else :
		overlay = resizeimage.resize_crop(overlay, list(new_size))

new_img = Image.blend(background, overlay, 0.5)
new_img.save("blended.png", background.format)