# Import the necessary modules from the 
# Python image library.
from PIL import Image, ImageFilter



def copy_image(input_image_file_name, output_image_file_name):
	"""
	Create a copy of an image by iterating over each pixel
	in the image in file input_image_file_name and copying
	the pixel to the image that will be stored in 
	output_image_file_name.
	"""
	# Use the open function to open the file containing
	# the image.
	input_image = Image.open(input_image_file_name)

	# Access the size property. This returns a tuple that is the
	# width and height of the image.
	image_width, image_height = input_image.size


	# Create a new RGB image the same size as the original.
	output_image = Image.new('RGB', (image_width, image_height))

	# Iteratve over every pixel in the image starting at position 
	# 0, 0.
	for i in range(image_width):
		for j in range(image_height):
        	# retrive the r, g, b values for the pixel
        	# at position i, j in the input image
			pixel_colors = input_image.getpixel((i, j))
            # set the rgb values for the pixel at 
            # position i, j in the output image
			output_image.putpixel((i, j), pixel_colors)

	output_image.save(output_image_file_name)

# Example of how to call the copy_image function.
copy_image('photo.jpeg', 'output.jpeg')
