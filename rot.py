# On terminal, you should use:
# pip install Pillow

from PIL import Image
import numpy
import math

# import filter.rotation

# Input image
input_image = Image.open('_lena.png')
width, height = input_image.size
print('> Opened image from path \'{0}\' (width = {1}, height = {2})'.format(input_image.fp.name, width, height))

rgb_channels_size = 3  # 3 because means RGB. Do not change this!

# Generate a matrix filled with 0 value
rgb_matrix = numpy.zeros((height, width, rgb_channels_size))

'''
#### Fill RGB matrix with pixels from input_image #####
for y in range(height):
    for x in range(width):
        pixel = input_image.getpixel((x, y))
        rgb_matrix[y, x] = pixel  # (r, g, b)
print('RGB matrix received image.')
#######################################################
'''

extended_matrix = numpy.zeros((round(height * 1.5), round(width * 1.5), rgb_channels_size))

################################### Image rotation - direct mapping ####################################
ic = 30
jc = 30
theta = math.radians(17)
rotation_matrix = numpy.copy(extended_matrix)

for y in range(height):
    for x in range(width):
        original_pixel = input_image.getpixel((x, y))
        print(input_image.getpixel((x, y)))

        # toY = max(0, min(round((x - ic)*math.sin(-theta) + (y - jc)*math.cos(-theta) + jc), height-1))
        # toX = max(0, min(round((x - ic)*math.cos(-theta) - (y - jc)*math.sin(-theta) + ic), width-1))

        toY = round((x - ic) * math.sin(-theta) + (y - jc) * math.cos(-theta) + jc)
        toX = round((x - ic) * math.cos(-theta) - (y - jc) * math.sin(-theta) + ic)

        toY = toY + 200
        toX = toX + 100

        rotation_matrix[toY, toX] = original_pixel
print()
##########################################################################################################

Image.fromarray(rotation_matrix.astype('uint8')).save('new_image.png')
print('New image saved.')

# Image Rotation based on angle 'theta' and center of rotation (ic, jc)
'''
print('Saving rotated image ...')
rotation_matrix = numpy.copy(rgb_matrix)
rotation_matrix = filter.rotation.rotate_image(rotation_matrix, 255, 255, math.radians(33))
Image.fromarray(rotation_matrix.astype('uint8')).save('results/rotated_image.png')
print('Rotated image saved.')
'''
